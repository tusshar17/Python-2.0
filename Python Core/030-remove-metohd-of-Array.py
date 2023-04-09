# remove(element) method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 103, 105])

for element in stu_roll:
    print(element)

# remove 103 from array

stu_roll.remove(103)

print("Array after removing 103")

for element in stu_roll:
    print(element)
