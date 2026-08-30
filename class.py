"""
定义一个学生类
要求：
1.属性包括学生姓名，学号，以及语数英三科成绩
2.能够设置学生某科目的成绩
3.能够打印出该学生的所有科目成绩
"""

class Student:
    def __init__(self,name,student_id):
        self.name=name
        self.student_id=student_id
        self.grades={"语文":0,"数学":0,"英语":0}

    def set_grade(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade

    def print_giades(self):
        print(f"学生{self.name}(学号：{self.student_id})的成绩为")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}分")

chen = Student("小陈","10086")
chen.set_grade("语文",92)
chen.set_grade("数学",94)
chen.print_giades()

# chen=Student("小陈","10086")
# zhang=Student("小张","10087")
# zhang.set_grade("数学",95)
# print(chen.name)
# print(zhang.grades)
