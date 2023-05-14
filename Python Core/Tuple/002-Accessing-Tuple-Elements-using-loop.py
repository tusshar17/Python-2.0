# Accessing Tuple Elements using Loop

a = 10, 20, -21.3, "hello"

# without index
for x in a:
    print(x)

# with index
for i in range(len(a)):
    print(i, ":", a[i])
