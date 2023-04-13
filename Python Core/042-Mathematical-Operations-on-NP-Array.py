# Mathematical Operations on NP Arrays

from numpy import *

a = array([101, 102, 103, 104, 105])
print("Original Array:", a)
a += 50
print("After Adding 50:", a)

a = array([1, 2, 3, 4, 5])
print("Array A:", a)
b = array([10, 20, 30, 40, 50])
print("Array B:", b)
c = a+b
print("Array C (Sum of A & B):", c)
