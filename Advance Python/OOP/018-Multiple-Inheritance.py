# Multiple Inheritance
# MRO - Method Resolution Order

class Father:
    def __init__(self) -> None:
        super().__init__()
        print("Father Class Constructor")

    def showF(self):
        print("Father Class Method")


class Mother:
    def __init__(self) -> None:
        super().__init__()
        print("Mother Class Constructor")

    def showM(self):
        print("Mother Class Method")


class Son(Father, Mother):
    def __init__(self) -> None:
        super().__init__()
        print("Son Class Constructor")

    def showS(self):
        print("Son Class Method")


s = Son()
s.showS()
s.showF()
s.showM()