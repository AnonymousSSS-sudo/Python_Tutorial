def remove_duplicates(lst: list) -> list:
    """
    去除列表中的重复元素，保留第一次出现的顺序
    """
    lst_ext = []
    for e in lst:
        if e not in lst_ext:
            lst_ext.append(e)
    return lst_ext

if __name__ == '__main__':
    lst = remove_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
    print(lst)