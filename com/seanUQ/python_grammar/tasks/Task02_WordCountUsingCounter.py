### 🟡 第 2 题 — 字典统计词频
from collections import Counter
from os.path import split
from typing import Collection


def word_count(sentence: str) -> dict:
    """
    统计字符串中每个单词出现的次数
    返回：按出现次数从多到少排序的字典
    """
    return dict(Counter(sentence.split()).most_common())


# │ 💬 提示： dict.get()
# 方法
# 或
# collections.Counter
# 可以帮你

if __name__ == '__main__':

    # 测试
    text = "apple banana apple cherry banana apple"
    print(word_count(text))