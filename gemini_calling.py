# Gemini函式呼叫
# https://ai.google.dev/tutorials/function_calling_python_quickstart

# 導入包
import pathlib
import time
import copy

import google.generativeai as genai
import google.api_core.exceptions
import google.generativeai.types.generation_types
import google.ai.generativelanguage as glm

import inspect
import traceback

import basic_functions
from tool.text_processing import *

from dotenv import load_dotenv
import os

# 處理函數呼叫邏輯，並傳送訊息給聊天模組。
def handle_function_call(fc):
    """
    處理函數呼叫邏輯，並傳送訊息給聊天模組。

    参数：
    - fc: 函数調用
    """
    while fc:
      # try:
        if fc.name == 'sql_query' or fc.name == 'get_factory':
          result = model._tools.__call__(fc).function_response.response['result']
          response = chat.send_message(
            result)
        else:
          response = chat.send_message(
            glm.Content(
            parts=[glm.Part(
                model._tools.__call__(fc))]))
        fc = response.candidates[0].content.parts[0].function_call
    return response

# 聊天訊息傳送
def send(chat, message):
    error_num = 0
    tmpe_chat = copy.copy(chat)
    while error_num < 5:
      try:
        response = chat.send_message(message)

        fc = response.candidates[0].content.parts[0].function_call
        if fc:
          response = handle_function_call(fc)
        
        return response
      except Exception as e:
        # 顯示錯誤訊息
        print("error", "->", e)
        traceback.print_exc()
        if len(chat.history) > 0:
          content = chat.history[-1]
          part = content.parts[0]
          print(content.role, "->", type(part).to_dict(part))
        
        chat = copy.copy(tmpe_chat)

        error_num += 1
        if error_num < 5:
           time.sleep(error_num)
    return None


# 設置您的API密鑰
# 加载.env文件中的环境变量
load_dotenv()
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)


# Set up the model
generation_config = {
  "temperature": 0,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


# 取得模組中的所有函數
all_functions = inspect.getmembers(basic_functions, inspect.isfunction)

# 提取函數並保存到列表中
all_function = [func for func_name, func in all_functions]


model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest',
                              generation_config=generation_config,
                              safety_settings=safety_settings,
                              tools=all_function)
# print(model._tools.to_proto())

chat = model.start_chat()
# chat = model.start_chat(enable_automatic_function_calling=True)

# send(chat, 'DB資料結構')
# send(chat, 'SQL查詢，Vendor前十筆')

# Chat
try:
  while True:
    user_input = input("user -> ")
    print('-'*80)
    if not user_input:
        print("end -> 輸入字串為空，程式結束。")
        break
    
    response = send(chat, user_input)

    try:
      if response is not None:
        print("model -> " + process_text(response.text))
      else:
        print("error -> None")
    except ValueError as err:
      print(f"response -> {response}")
      print(f"error -> {err}")
    print('-'*80)
finally:
  # 查詢步驟
  print('='*80)
  print('查詢步驟')
  print('='*80)
  for content in chat.history:
      part = content.parts[0]
      print(content.role, "->", type(part).to_dict(part))
      print('-'*80)