# Generator Function


def display(a, b):
    yield a
    yield b


x, y = display(50, 100)
print(x, y)

print()

res = display(10, 20)
print(res)
print(type(res))

print()

lst = list(res)
print(lst)

print()

res2 = display(11, 22)
print(next(res2))
print(next(res2))

print()


def nums(limit):
    for a in range(limit):
        yield a


res3 = nums(10)
print(next(res3))
print(next(res3))
print("-")
for i in res3:
    print(i)
