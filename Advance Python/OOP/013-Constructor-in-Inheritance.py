# Constructor in Inheritance


class Father:
    def __init__(self) -> None:
        self.money = 500000
        print("Father class constructor")

    def show(self):
        print("Father instance method")


class Son(Father):
    def display(self):
        print("Son instance method")


s = Son()
print(s.money)
