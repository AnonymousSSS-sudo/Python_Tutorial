def modify(lst):
    lst.append(99)
    lst = [0,0,0,0]
    # return lst

if __name__ == '__main__':
    # data = modify([1,2,3,4,5])
    data = [1,2,3,4,5]
    modify(data)
    print(data)
