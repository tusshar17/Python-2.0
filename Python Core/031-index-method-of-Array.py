# index(element) method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 103, 105])

for element in stu_roll:
    print(element)

# find the index of element '103'
print("index:", stu_roll.index(103))
