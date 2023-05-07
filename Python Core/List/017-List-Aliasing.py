# List Aliasing

a = [10, 20, 30, 40, 50]

b = a

print("Before Any Modification:")
print("A:", a)
print("B:", b)

a[0] = 0

print("Modified A:")
print("A:", a)
print("B:", b)

b[1] = 0

print("Modified B:")
print("A:", a)
print("B:", b)
