'''
### 🟠 第 4 题 — 列表 + 字典：成绩分析器

students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob", "score": 78},
    {"name": "Charlie", "score": 85},
    {"name": "David", "score": 60},
    {"name": "Eve", "score": 95},
]


def analyze_scores(students: list) -> dict:
    """
    返回一个字典，包含：
    - "highest": 最高分学生的名字
    - "lowest":  最低分学生的名字
    - "average": 平均分（保留1位小数）
    - "passed":  及格（>=60）的学生名单（列表）
    """
    ???

    result = analyze_scores(students)
    print(result)
    # 期望输出：
    # {
    #   "highest": "Eve",
    #   "lowest": "David",
    #   "average": 82.0,
    #   "passed": ["Alice", "Bob", "Charlie", "David", "Eve"]]
    # }
'''
from audioop import avg

'''
获取对应信息 整理成字典
'''
def analyze_scores(students: list) -> dict:
    # 最高分
    highest_student = max(students, key=lambda student: student["score"])
    highest_student_name = highest_student["name"]
    # 最低分
    lowest_student = min(students, key=lambda student: student["score"])
    lowest_student_name = lowest_student["name"]
    # 均分 保留一位小数
    average_score = round(sum(student["score"] for student in students) / len(students), 1)
    # 通过人数
    passed_students = [student for student in students if student["score"] >= 60]
    passed_count = len(passed_students)

    # score_info = {}
    # score_info["highest"] = highest_student_name
    # score_info["lowest"] = lowest_student_name
    # score_info["average"] = average_score
    # score_info["passed"] = passed_count
    return {
        "highest": highest_student_name,
        "lowest": lowest_student_name,
        "average": average_score,
        "passed": passed_count
    }

if __name__ == '__main__':

    students = [
        {"name": "Alice", "score": 92},
        {"name": "Bob", "score": 78},
        {"name": "Charlie", "score": 85},
        {"name": "David", "score": 60},
        {"name": "Eve", "score": 95},
    ]

    print(analyze_scores(students))


