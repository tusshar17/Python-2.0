# Single Inheritance.py


class Father:
    money = 1000

    def __init__(self) -> None:
        print("Constructor of Father class called")

    def show(self):
        print("Instance method of Father class")

    @classmethod
    def show_money(cls):
        print("Parent class ClassMethod:", cls.money)

    @staticmethod
    def stat():
        x = 10
        print("Static method of parent class:", x)


class Son(Father):
    def __init__(self) -> None:
        print("Constructor of Son class called")

    def display(self):
        print("Instance method of Child class")


s = Son()
s.display()
s.show()
s.show_money()
s.stat()
