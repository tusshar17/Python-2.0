# Passing Member of one Class to Another


class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch


class User:
    @staticmethod
    def show_details(s):
        print("User Name:", s.name)
        print("User Branch:", s.branch)


stu = Student("Joy", "CSE")
User.show_details(stu)
