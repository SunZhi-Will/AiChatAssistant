import functools
import inspect
import os
import re
from typing import Any, Callable, Dict, List, Optional
import logging
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

import basic_functions
from core.azure_functions import AzureOpenAIFunctions

logger = logging.getLogger(__name__)

load_dotenv()

# 取得模組中的所有函數
all_functions = inspect.getmembers(basic_functions, inspect.isfunction)

# 提取函數並保存到列表中
all_function = [func for func_name, func in all_functions]

assistant = AzureOpenAIFunctions(
    azure_openai_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_openai_key_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_api_version="2024-03-01-preview",
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    functions=all_function
)
messages = []
while True:
    user_input = input("Enter a message (or press Enter to exit): ")
    if not user_input:
        break
    messages.append({"role": "user", "content": user_input})

    response = assistant.ask(messages)
    response_message = response.choices[0].message.content
    print(response_message)