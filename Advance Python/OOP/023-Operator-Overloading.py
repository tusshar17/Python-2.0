# Operator Overloading

'''
print(10 + 20)
print(int.__add__(10, 20))

print('10' + '20')
print(str.__add__('10', '20'))
'''

class A:
    def __init__(self, x) -> None:
        self.x = x

    def __add__(self, other):
        return self.x + other.x
    

class B:
    def __init__(self, x) -> None:
        self.x = x


a = A(10)
b = B(20)

print(a + b)  # A.__add__(a, b)
