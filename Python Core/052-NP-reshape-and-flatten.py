# reshape() Function

import numpy as np

# 1D to 2D
print("1D to 2D")
a = np.array([1, 2, 3, 4, 5, 6])
b = np.reshape(a, (2, 3))
print("A:\n", a)
print("B:\n", b)

print('-'*15)

# 1D to 3D
print("1D to 3D")
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d = np.reshape(c, (2, 2, 3))
print("C:\n", c)
print("D:\n", d)

print('-'*15)

# 2D to 1D
print("2D to 1D")
e = np.array([[1, 2, 3], [4, 5, 6]])
f = np.reshape(e, (6))
print("E:\n", e)
print("F:\n", f)

print('-'*15)


# flatten() Method
print("flatten() Method")
a = np.array([[1, 2, 3], [4, 5, 6]])
b = b.flatten()
print("A:\n", a)
print("B:\n", b)
