# Copying

a = [10, 20, 30, 40, 50]
b = a.copy()

print("A:", a)
print("B:", b)

print()
a[0] = 99
print("Modified A:")
print("A:", a)
print("B:", b)

print()
b[-1] = 99
print("Modified B:")
print("A:", a)
print("B:", b)
print()

# Cloning
print("====Cloning====")
a = [10, 20, 30, 40, 50]
b = a[:]

print("A:", a)
print("B:", b)

print()
a[0] = 99
print("Modified A:")
print("A:", a)
print("B:", b)

print()
b[-1] = 99
print("Modified B:")
print("A:", a)
print("B:", b)
