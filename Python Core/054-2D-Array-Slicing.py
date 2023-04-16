# Numpy 2D Array Slicing

import numpy as np

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("Original Array:")
print(a)

print("0th row, all columns")
print(a[0, :])

print("middle elements")
print(a[1:3, 1:3])

print("alternate rows and columns")
print(a[::2, ::2])
