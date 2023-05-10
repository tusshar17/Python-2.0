# Nested List

a = [10, 20, 30, [50, 60]]

print("a:", a)

print()

b = [50, 60]
a = [10, 20, 30, b]
print("a:", a)

print()

c = [[1, 2, 3, 4], [5, 6, 7, 8]]
print("c:", c)

print()

# Accessing Nested List
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[3][0]:", a[3][0])
print("a[3][1]:", a[3][1])

print()


# Modifying Nested List
print("a (before):", a)
a[1] = 100
a[3][0] = 5
print("a (after):", a)
