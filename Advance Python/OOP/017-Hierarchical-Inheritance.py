# Hierarchical Inheritance

class Father:
    def __init__(self) -> None:
        print("Father Class Constructor")

    def showF(self):
        print("Father class method")


class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("Son Class Constructor")

    def showS(self):
        print("Son class method")


class Daughter(Father):
    def __init__(self) -> None:
        super().__init__()
        print("Daughter Class Constructor")

    def showD(self):
        print("Daughter class method")


s = Son()
s.showS()
s.showF()

print()

d = Daughter()
d.showD()
d.showF()