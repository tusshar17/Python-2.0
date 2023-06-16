# Constructor with super() method

class Father:
    def __init__(self, m) -> None:
        self.money = m
        print("Father Class Constructor")

    def show(self):
        print("Father Class Instance method")


class Son(Father):
    def __init__(self, m, j) -> None:
        super().__init__(m)
        self.money = 1000
        self.job = j
        print("Son Class Constructor")

    def display(self):
        print("Son Class Instance method")
        print("Money:", self.money)
        print("Job:", self.job)


s = Son(10000, "Django")
s.display()