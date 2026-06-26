'''
### 🟡 第 3 题 — 集合求交集/差集应用

# 有两组学生选课数据
course_a = {"Alice", "Bob", "Charlie", "David"}
course_b = {"Bob", "David", "Eve", "Frank"}

# 请用集合操作完成以下三个问题（每题一行代码）：

# 问题1：同时选了两门课的学生？
both = ???

# 问题2：只选了课程A、没选课程B的学生？
only_a = ???

#

print(both)  # {'Bob', 'David'}
print(only_a)  # {'Alice', 'Charlie'}
print(total)  # 6
'''

'''
问题1：同时选了两门课的学生？
both = ???
'''
def queryIntersaction(course_a:set, course_b:set) -> int:
    # return len(course_a & course_b)
    # 返回的是两个集合交集的大小
    return len(course_a.intersection(course_b))

'''
问题2：只选了课程A、没选课程B的学生？
only_a = ???
'''
def queryDifference(course_a:set, course_b:set) -> int:
    # 返回的是差集的大小
    return len(course_a.difference(course_b))

'''
问题3：两门课加起来总共有多少不重复的学生？
total = ???
'''
def queryUnion(course_a:set, course_b:set) -> int:
    return len(course_a.union(course_b))


if __name__ == '__main__':
    course_a = {"Alice", "Bob", "Charlie", "David"}
    course_b = {"Bob", "David", "Eve", "Frank"}
    print(f"both is: {queryIntersaction(course_a, course_b)}")
    print(f"only_a is: {queryDifference(course_a, course_b)}")
    print(f"total is: {queryUnion(course_a, course_b)}")
