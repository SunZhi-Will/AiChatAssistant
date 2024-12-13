import json
import matplotlib.pyplot as plt
import numpy as np

from tool.text_processing import process_text


def get_bar(data, title):
    '''
    data範例:
    {
        "left": [1, 2, 3, 4, 5],
        "bars":[{"height":[10, 30,50, 20, 33], "color": 'blue'},{"height":[21, 31,45, 35, 77], "color": 'red'}],
        "labels":['apple', 'banana', 'coconut', 'dragon fruit', 'eggplant'],
    }
    '''
    # left = np.array([1, 2, 3, 4, 5])
    # height1 = np.array([10, 30,50, 20, 33])
    # height2 = np.array([21, 31,45, 35, 77])

    # labels = ['apple', 'banana', 'coconut', 'dragon fruit', 'eggplant']

    #選擇要在下面的棒狀圖 blue
    for bar in data['bars']:
        plt.bar(data['left'], bar['height'], color=bar['color'], tick_label=data['labels'])

    #選擇要在上面的棒狀圖 red
    # plt.bar(left, height2, bottom=height1, color='red', tick_label=labels)

    plt.title(process_text(title), fontproperties='SimSun')
    plt.legend()
    plt.show()

def get_chart(data, title, xtext, ytext, xticks_name, plot_labels:dict):
    if 'result' in data:
            data = data['result'] 
    print(data)
    # 提取各种数据
    years = [entry[xticks_name] for entry in data]
    plot_labels = convert_to_dict(plot_labels)
    data_items = list(plot_labels.keys())
    if xticks_name in data_items:
        data_items.remove(xticks_name)  # 排除年份列
    

    # 创建线图
    fig, ax = plt.subplots()

    # 循环绘制数据项的线图
    for item in data_items:
        values = [entry[item] for entry in data]
        ax.plot(years, values, label=process_text(plot_labels[item]))

    plt.rcParams['font.sans-serif'] = ['SimSun']  # 设置字体为宋体
    plt.xlabel(process_text(xtext))
    plt.ylabel(process_text(ytext))
    plt.title(process_text(title))
    plt.legend()
    plt.grid(True)
    plt.xticks(years)  # 设置 x 轴刻度为年份
    plt.show()

def convert_to_dict(labels):
    # 如果标签已经是字典，则直接返回
    if isinstance(labels, dict):
        return labels
    
    # 将字符串标签转换为字典
    try:
        label_dict = json.loads(labels)
        
        return label_dict
    except:
        return labels

# json_data = '''{"left": [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030], "bars":[{"height":[5100, 4458.2, 0, 0, 0, 0, 0, 0, 0], "color": "blue"}, {"height":[0, 81.8, 5450, 5611, 5431, 5454, 5466, 5469, 5805], "color": "red"}, {"height":[0, 132, 634, 901, 1098, 1092, 1086, 1080, 1074], "color": "green"}], "labels":[2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]}'''
# if isinstance(json_data, str):
#     # 取消所有 \\ 并将 \" 改为 "
#     json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
#     print(json_data)
#     # 解析 JSON 数据
#     data = json.loads(json_data)
                
# else:
#     # 将 JSON 数据对象转换为字符串
#     if 'result' in json_data:
#         json_data = json.dumps(json_data['result'])
#     else:
#         json_data = json.dumps(json_data)
#     # print(json_data)
#     json_data = json_data.replace("\\\\", "").replace("\\\"", "\"").replace("\"[{", "[{").replace("}]\"", "}]")
#     # print(json_data)
#     data = json.loads(json_data)
# get_bar(data)