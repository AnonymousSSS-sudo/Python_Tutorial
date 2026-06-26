### 🟡 第 2 题 — 字典统计词频
from typing import Collection


def word_count(sentence: str) -> dict:
    """
    统计字符串中每个单词出现的次数
    返回：按出现次数从多到少排序的字典
    """
    str_list = sentence.split()
    dict_count = {}
    # for word in str_list:
    #     if word not in dict_count:
    #         dict_count[word] = 1
    #     else:
    #         dict_count[word] += 1
    for word in str_list:
        '''
           dict.get(key, default)  的含义：
           若  key  不存在 → 返回  default （不会抛出 KeyError）
           在词频统计中，它解决的核心问题是：
           第一次遇到某个单词时，字典里还没有它，
           如果直接 dict[word] += 1 → ❌ KeyError
           用 dict.get(word, 0) + 1 → ✅ 默认从 0 开始计数
        '''
        dict_count[word] = dict_count.get(word, 0) + 1

    # 按照当前 item 值对字典内容进行逆序排序
    return dict(sorted(dict_count.items(), key=lambda x: x[1], reverse=True))


# │ 💬 提示： dict.get()
# 方法
# 或
# collections.Counter
# 可以帮你

if __name__ == '__main__':

    # 测试
    text = "apple banana apple cherry banana apple"
    print(word_count(text))
    # 期望输出：{'apple': 3, 'banana': 2, 'cherry': 1}
    # word_count(text)