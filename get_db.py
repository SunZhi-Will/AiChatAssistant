# import sqlite3

# # 连接到SQLite数据库
# conn = sqlite3.connect('./db/data.db')
# cursor = conn.cursor()

# # 执行SQL查询
# cursor.execute('SELECT * FROM my_table')
# rows = cursor.fetchall()

# # 打印查询结果
# for row in rows:
#     print(row)

# # 获取my_table的结构信息
# cursor.execute("PRAGMA table_info(my_table)")
# columns = cursor.fetchall()

# # 打印表结构
# print("Table structure for my_table:")
# for column in columns:
#     print(column[1], "-", column[2])

# # 关闭连接
# conn.close()

