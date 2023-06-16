# Constructor Overriding


class Father:
    def __init__(self) -> None:
        self.money = 50000
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance method")


class Son(Father):
    def __init__(self) -> None:
        self.money = 1000
        self.car = "Tata"
        print("Son Class Constructor")

    def display(self):
        print("Son Class Instance method")


s = Son()
print(s.money)
print(s.car)
s.display()
s.show()

print("---------")

f = Father()
