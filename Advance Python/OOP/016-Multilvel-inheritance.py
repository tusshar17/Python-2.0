# Multilevel Inheritance

class Father:
    def __init__(self) -> None:
        print("Father Class Constructor")

    def showF(self):
        print("Father Class Method")


class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("Son Class Constructor")

    def showS(self):
        print("Son Class Method")


class GrandsSon(Son):
    def __init__(self) -> None:
        super().__init__()
        print("Grand Son Class Constructor")

    def showG(self):
        print("Grand Son Class Method")


g = GrandsSon()
g.showG()
g.showS()
g.showF()