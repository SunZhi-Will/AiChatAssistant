import sqlite3
import csv

# 从CSV文件中获取唯一的列名
def get_unique_column_names(filename):
    unique_headers = []  # 用于存储唯一的列名
    seen_headers = set()  # 用于跟踪已经出现过的列名
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # 获取标题行
        for header in headers:
            # 如果列名是首次出现，则添加到列表中
            if header not in seen_headers:
                unique_headers.append(header)
                seen_headers.add(header)
    return unique_headers

# 创建SQL表
def create_table(cursor, table_name, column_names):
    # 构建CREATE TABLE语句
    sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} ("
    for column in column_names:
        sql_query += f"{column} TEXT,"
        print(column)
    sql_query = sql_query[:-1] + ")"  # 去掉最后一个逗号并添加右括号
    print(sql_query)
    cursor.execute(sql_query)

# 将数据插入SQL表
def insert_data(cursor, table_name, filename):
    with open(filename, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # 跳过标题行
        for row in csvreader:
            # 检查数据行的列数是否与表的列数匹配
            if len(row) != len(column_names):
                print(f"Ignoring row: {row} as column count doesn't match")
                # continue
                row.extend([''] * (len(column_names) - len(row)))
            cursor.execute(f"INSERT INTO {table_name} VALUES ({','.join('?' * len(row))})", row)

# 连接到SQLite数据库
conn = sqlite3.connect('./db/data.db')
cursor = conn.cursor()

# 获取CSV文件的唯一列名
csv_filename = './data/data.csv'
column_names = get_unique_column_names(csv_filename)

# 创建SQL表
table_name = 'my_table'
create_table(cursor, table_name, column_names)

insert_data(cursor, table_name, csv_filename)

# 获取CSV文件的唯一列名
csv_filename = './data/data1.csv'
column_names = get_unique_column_names(csv_filename)

# 创建SQL表
table_name = 'my_table1'
create_table(cursor, table_name, column_names)

# 将数据插入SQL表
insert_data(cursor, table_name, csv_filename)

# 提交更改并关闭连接
conn.commit()
conn.close()
