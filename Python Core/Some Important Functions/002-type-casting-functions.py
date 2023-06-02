# type casting functions

# int()
print("=====int()=====")
a = 10.56
print("Float:", a)
print(type(a))

new_a = int(a)
print("Int:", new_a)
print(type(new_a))
print()

b = "10"
print("String:", b)
print(type(b))

new_b = int(b)
print("Int:", new_b)
print(type(new_b))
print()

# c = "Hello"
# print("String:", c)
# print(type(c))

# # new_c = int(c)  --> ValueError: invalid literal for int() with base 10: 'Hello'
# print("Int:", new_c)
# print(type(new_c))
# print()


# float()
print("=====float()=====")
a = 10
print("Int:", a)
print(type(a))

new_a = float(a)
print("Float:", new_a)
print(type(new_a))
print()

b = "10.56"
print("String:", b)
print(type(b))

new_b = float(b)
print("Float:", new_b)
print(type(new_b))
print()

# c = "Hello"
# print("String:", c)
# print(type(c))

# new_c = float(c)  # --> ValueError: could not convert string to float: 'Hello'
# print("Float:", new_c)
# print(type(new_c))
# print()

# str()
print("=====str()=====")
a = 10
print("Int:", a)
print(type(a))

new_a = str(a)
print("str:", new_a)
print(type(new_a))
print()

b = 10.56
print("Float:", b)
print(type(b))

new_b = str(b)
print("str:", new_b)
print(type(new_b))
print()


c = [1, 2, 3]
print("List:", c)
print(type(c))

new_c = str(c)
print(new_c, type(new_c))
print(new_c[0])
print()


# list()
print("=====list()=====")
a = (10, 20, 30)
print(a, type(a))

new_a = list(a)
print(new_a, type(new_a))
print()

b = {10, 20, 30}
print(b, type(b))

new_b = list(b)
print(new_b, type(new_b))
print()

c = {10: "a", 20: "b", 30: "c"}
print(c, type(c))

new_c = list(c)
print(new_c, type(new_c))
print()

d = "hello"
print(d, type(d))

new_d = list(d)
print(new_d, type(new_d))
print()


# tuple()
print("=====tuple()=====")
a = [10, 20, 30]
print(a, type(a))

new_a = tuple(a)
print(new_a, type(new_a))
print()

b = {10, 20, 30}
print(b, type(b))

new_b = tuple(b)
print(new_b, type(new_b))
print()

c = {10: "a", 20: "b", 30: "c"}
print(c, type(c))

new_c = tuple(c)
print(new_c, type(new_c))
print()

d = "hello"
print(d, type(d))

new_d = tuple(d)
print(new_d, type(new_d))
print()


# set()
print("=====set()=====")
a = [10, 20, 30]
print(a, type(a))

new_a = set(a)
print(new_a, type(new_a))
print()

b = (10, 20, 30)
print(b, type(b))

new_b = set(b)
print(new_b, type(new_b))
print()

c = {10: "a", 20: "b", 30: "c"}
print(c, type(c))

new_c = set(c)
print(new_c, type(new_c))
print()

d = "hello"
print(d, type(d))

new_d = set(d)
print(new_d, type(new_d))
print()


# dict()
print("=====set()=====")
a = [(1, "a"), (2, "b"), (3, "c")]
print(a, type(a))

new_a = dict(a)
print(new_a, type(new_a))
