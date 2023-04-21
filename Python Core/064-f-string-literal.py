# f string literals


# Integer

a = 10
b = 20

# print(f"{}") --> cna't left empty
print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")
print(f"{a}       {b}")
print()


# Float

a = 10.15
b = 20.35

print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")
print()


# String

a = "Hello"
b = "World"

print(f"{a}")
print(f"{a} {b}")
print(f"{b} {a}")
print()


# String and int

name = "Rahul"
age = 15

print(f"My name is {name} and my age is {age}")
print()


# advance formatting
num = 15

print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print()

num = 15.65

print(f"{num:8f}")
print(f"{num:8.3f}")
print(f"{num:+8.2f}")
print(f"{num:<8.2f}")
print(f"{num:*<8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print()


name = "Hello"

print(f"{name:8s}")
print(f"{name:<8s}")
print(f"{name:*<8s}")
print(f"{name:>8s}")
print(f"{name:*>8s}")
print(f"{name:^8s}")
print()

print(f"{name:.3s}")
print(f"{name:8.3s}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3s}")
print()


price = 1234567890
print(f"{price:,}")
print(f"{price:_}")
