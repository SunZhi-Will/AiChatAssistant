import textwrap

from IPython import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# 字串編碼
def process_text(text):
    """
        處理文字並傳回結果。

        參數：
        - text: 待處理的文本

        返回：
        - 處理後的文字結果
    """
    # 按照分隔符 \\ 拆分字符串成列表
    notices = text.split('\\')

    result = notices[0]
    first_three_chars = ""

    import ast
    for i, notice in enumerate(notices[1:], start=1):
        if len(notice) > 3:
            first_three_chars += "\\" + notice[:3]
            le = ast.literal_eval(f'b"{first_three_chars}"').decode('utf-8')
            result += le + notice[3:]
            first_three_chars = ""
        else:
            first_three_chars += "\\" + notice

    le = ast.literal_eval(f'b"{first_three_chars}"').decode('utf-8')
    result += le
    first_three_chars = ""
    return result