import json
import tool.text_processing as text_processing 
import requests

import tool.chart as chart

URL = 'http://localhost:8082/rest/PublicService/v1/'

# 功能基礎
def get_datetime(timezone:str):
    """
    :param timezone: The Time zone.
    :returns datetime now.
    """
    from datetime import datetime
    import pytz
    return datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d %H:%M:%S")
def get_date(timezone:str):
    """returns date now."""
    from datetime import datetime
    import pytz
    return datetime.now(pytz.timezone(timezone)).strftime("%Y-%m-%d")

# SQL
def get_db_structure():
    """returns DB Structure."""
    import sqlite3
    # 连接到SQLite数据库
    conn = sqlite3.connect('./db/data.db')
    cursor = conn.cursor()

    # 获取数据库中所有表的名称
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    text = ""
    # 遍历所有表，并获取其结构信息
    for table in tables:
        table_name = table[0]
        text += f"Table structure for {table_name}:\n"

        # 获取表结构信息
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        # 打印表结构信息
        for column in columns:
            text += column[1] + "-" + column[2] + '\n'

        text += '\n'

    # 关闭连接
    conn.close()
    return text

def sql_query(query:str):
    """
    query:str 格式為"SELECT * FROM my_table"

    Notice is 注意事項
    returns SQL query results.
    """
    import sqlite3
    while query.startswith('"') and query.endswith('"'):
        # 去除双引号
        query = query[1:-1]
    query = text_processing.process_text(query)

    # 连接到SQLite数据库
    conn = sqlite3.connect('./db/data.db')
    cursor = conn.cursor()

    # 执行SQL查询
    cursor.execute(query)
    rows = cursor.fetchall()

    # 打印查询结果
    text = f'顯示查詢結果:\n'
    for row in rows:
        text += f'{row},'
        # print(row)

    # 关闭连接
    conn.close()
    return text

# API
def get_factory():
    """
    讀取所有公司及廠區
    """
    url = URL + 'factory'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return "Error:", response.status_code
    
def get_renewenergytrend():
    """
    讀取再生能源 趨勢
    """
    url = URL + 'renewenergytrend'
    headers = {'accept': 'application/json'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return "Error:", response.status_code

# 圖表
def generate_graph(json_data:str,title:str, xtext:str, ytext:str, xticks_key:str, plot_labels:dict):
    """
    以json字串產生圖表

    將資料轉成json字串
    不需要格式排列
    範例:
    {"result": "[{"Year":2024...

    title 為圖表標題
    plot_labels 為dict
    將需要顯示在圖表中的Key跟Label寫入
    範例:
    {"Year":"年",....
    """
    # print(json_data)
    if isinstance(json_data, str):
        # 取消所有 \\ 并将 \" 改为 "
        json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
        # print(json_data)
        # 解析 JSON 数据
        data = json.loads(json_data)
                    
    else:
        # 将 JSON 数据对象转换为字符串
        if 'result' in json_data:
            json_data = json.dumps(json_data['result'])
        else:
            json_data = json.dumps(json_data)
        # print(json_data)
        json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
        # print(json_data)
        data = json.loads(json_data)
    chart.get_chart(data, title, xtext, ytext, xticks_key, plot_labels)
    return "已產生圖表圖片"


def get_bar(json_data:str, title:str):
    """
    以json字串產生柱狀圖表
    
    title 為圖表標題
    json_data範例:
    {"left": [2022], "bars":[{"height":[5100], "color": "blue"}, {"height":[0], "color": "red"}], "labels":["2022"]}
    """
    if isinstance(json_data, str):
        # 取消所有 \\ 并将 \" 改为 "
        json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
        # print(json_data)
        # 解析 JSON 数据
        data = json.loads(json_data)
                    
    else:
        # 将 JSON 数据对象转换为字符串
        if 'result' in json_data:
            json_data = json.dumps(json_data['result'])
        else:
            json_data = json.dumps(json_data)
        # print(json_data)
        json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
        # print(json_data)
        data = json.loads(json_data)
    chart.get_bar(data, title)
    return "已產生圖表圖片"


