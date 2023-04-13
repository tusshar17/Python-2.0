# where function in numpy

import numpy as np

a = np.array([100, 200, 300, 400, 500])
b = np.array([10, 201, 30, 40, 50])
print("A:", a)
print("B:", b)

c = np.where(a > b, a, b)
print("C:", c)
