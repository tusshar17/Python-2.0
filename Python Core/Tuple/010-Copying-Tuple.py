# Copying Tuple

a = 10, 20, 30, 40, 50

b = a  # this is aliasing

print("a:", a)
print("id(a):", id(a))
print("b:", b)
print("id(b):", id(b))

print()

b = a[0:4] + (a[4],)
print("a:", a)
print("id(a):", id(a))
print("b:", b)
print("id(b):", id(b))
