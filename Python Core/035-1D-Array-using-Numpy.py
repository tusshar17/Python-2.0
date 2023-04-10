# 1D Array using Numpy

import numpy as np

stu_roll = np.array([101, 102, 103, 104, 105])

print(stu_roll)
print(stu_roll.dtype)

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])

# modifying element
stu_roll[0] = 110
print(stu_roll.dtype)

chars = np.array(['a', 'b', 'c', 'd', 'e', 5])
print(chars)
print(chars.dtype)
