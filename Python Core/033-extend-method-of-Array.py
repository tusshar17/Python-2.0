# extend(iterable_object) method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])
arr = array('i', [106, 107, 108])

print("Element in stu_roll before extending:")
for element in stu_roll:
    print(element)

# extending stu_roll with arr
stu_roll.extend(arr)

print("Element in stu_roll after extending:")
for element in stu_roll:
    print(element)
