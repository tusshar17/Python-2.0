# Tuple of List

a = (10, 20, 30, [40, 50])
print("Original Tuple:", a)
print("type(a):", type(a))
print("id(a):", id(a))
print()

# Modifying List
a[3][0] = 99
print("After modifying list's element:")
print("a:", a)
print("type(a):", type(a))
print("id(a):", id(a))
print()


# Accessing Tuple of List

# without index
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
