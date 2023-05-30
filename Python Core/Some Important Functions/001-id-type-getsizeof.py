a = 10
b = 10.23
c = "String"
d = [1, 2, 3]
e = (1, 2, 3)
f = {1, 2, 3}
g = {1: "a", 2: "b"}


# id() function

print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(id(e))
print(id(f))
print(id(g))


# type() function

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))


# getsizeof() function

import sys

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
print(sys.getsizeof(e))
print(sys.getsizeof(f))
print(sys.getsizeof(g))
