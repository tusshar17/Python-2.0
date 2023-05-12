# Accessing List Elements using For Loop

a = [10, 20, 30, 40, 50]

# without index
for x in a:
    print(x)


# with index
for x in range(len(a)):
    print(x, "index:", a[x])
