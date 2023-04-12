# Numpy 1D Array using logspace

from numpy import *

a = logspace(1, 3, 5)
for element in a:
    print(element)

print("-"*5)

b = logspace(1, 2, 5, base=12)
for element in b:
    print(element)
