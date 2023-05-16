# List of Tuple

a = [10, 20, 30, (40, 50)]
print("Original List:", a)
print("type(a):", type(a))
print("id(a):", id(a))

print()

# Appending a new Tuple

a.append((60, 70))
print("After appending a new Tuple:")
print("a:", a)
print("type(a):", type(a))
print("id(a):", id(a))
print()


# Accessing List of Tuple using loop

# without index
for x in a:
    if type(x) is tuple:
        for y in x:
            print(y)

    else:
        print(x)

print()

# with index
for x in range(len(a)):
    if type(a[x]) is tuple:
        for y in range(len(a[x])):
            print("[{}][{}] :".format(x, y), a[x][y])

    else:
        print("[{}] :".format(x), a[x])
