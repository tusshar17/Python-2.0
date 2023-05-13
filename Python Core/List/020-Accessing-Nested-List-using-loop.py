# Accessing Nested List Elements using For Loop

a = [10, 20, 30, [40, 50, 60]]

# without index

# for x in a:
# for y in x:    --> TypeError: 'int' object is not iterable
# print(y)


for x in a:
    if type(x) is list:
        for y in x:
            print(y)

    else:
        print(x)

print()

# with index
for x in range(len(a)):
    if type(a[x]) is list:
        for y in range(len(a[x])):
            print("[{}][{}] :".format(x, y), a[x][y])

    else:
        print("[{}] :".format(x), a[x])
