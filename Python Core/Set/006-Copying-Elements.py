# Copying Elements

a = {1, 2, 3, 4, 5, "hello"}
print("original set:", a)
print("id of original set:", id(a))

b = a.copy()
print("copied set:", b)
print("id of copied set:", id(b))
