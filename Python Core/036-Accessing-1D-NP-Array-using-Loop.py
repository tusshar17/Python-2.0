# Accessing NumPy 1D Array using for loop

import numpy as np

stu_roll = np.array([101, 102, 103, 104, 105])

# without index
for element in stu_roll:
    print(element)

print("-"*5)

# with index
n = len(stu_roll)
for i in range(n):
    print("index", i, ":", stu_roll[i])
