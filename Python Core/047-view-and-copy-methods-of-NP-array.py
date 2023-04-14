# view() and copy() methods of numpy array

import numpy as np

# view()
print("----view()--------")
a = np.array([10, 20, 30, 40, 50])
b = a.view()

print("A:", a)
print("B:", b)

print("ID of A:", id(a))
print("ID of B:", id(b))

a[0] = 0
b[-1] = 0
print("Value of a[0] and b[0] changed")

print("A:", a)
print("B:", b)


# copy()
print("----copy()--------")
a = np.array([10, 20, 30, 40, 50])
b = a.copy()

print("A:", a)
print("B:", b)

print("ID of A:", id(a))
print("ID of B:", id(b))

a[0] = 0
b[-1] = 0
print("Value of a[0] and b[0] changed")

print("A:", a)
print("B:", b)
