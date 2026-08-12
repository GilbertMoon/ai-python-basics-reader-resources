# Chapter 18 - 메서드 사용하기


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def show_result(self):
        print(f"{self.name}: {self.score}점")

    def is_passed(self):
        return self.score >= 60


student = Student("민수", 85)
student.show_result()
print(student.is_passed())
