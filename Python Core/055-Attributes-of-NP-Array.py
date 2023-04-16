# Attributes of Numpy Array

import numpy as np

a = np.array([10, 20, 30, 40])
b = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160]
])

print("1D Array:")
print(a)
print("2D Array:")
print(b)
print("-"*15)

# ndim
print("ndim of 1D Array:", a.ndim)
print("ndim of 2D Array:", b.ndim)
print("-"*15)

# shape
print("shape of 1D Array:", a.shape)
print("shape of 2D Array:", b.shape)
print("-"*15)

# size
print("size of 1D Array:", a.size)
print("size of 2D Array:", b.size)
print("-"*15)

# itemsize
print("itemsize of 1D Array:", a.itemsize)
print("itemsize of 2D Array:", b.itemsize)
print("-"*15)

# dtype
print("dtype of 1D Array:", a.dtype)
print("dtype of 2D Array:", b.dtype)
print("-"*15)

# nbytes
print("nbytes of 1D Array:", a.nbytes)
print("nbytes of 2D Array:", b.nbytes)
print("-"*15)
