def remove_duplicates(lst: list) -> list:
    """
    去除列表中的重复元素，保留第一次出现的顺序
    以列表元素为  key  构建字典（重复的 key 会被覆盖但不改变顺序）
    最后取出所有  key  即为去重且保序的结果
    """
    dict_ext = {}
    for item in lst:
        if item not in dict_ext:
            dict_ext[item] = 1
    # 从 dict 中取出所有key
    # print(type(keys))
    return list(dict_ext.keys())

if __name__ == '__main__':
    lst = remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(lst)