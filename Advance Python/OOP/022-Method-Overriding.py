# Method Overriding

class Add:
    def res(self, a, b):
        print("Add:", a+b)


class Mul(Add):
    def res(self, a, b):
        print("Multiply:", a*b)


obj = Mul()
obj.res(10, 20)

print()

# using super() method

class Divide(Add):
    def res(self, a, b):
        super().res(a, b)
        print("Divide:", a/b)

d = Divide()
d.res(20, 10)