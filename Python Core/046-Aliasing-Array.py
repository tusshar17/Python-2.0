# Alliasing Array

from numpy import *

a = array([10, 20, 30, 40, 50])
b = a

print("A:", a)
print("B:", b)

print("ID of A:", id(a))
print("ID of B:", id(b))
