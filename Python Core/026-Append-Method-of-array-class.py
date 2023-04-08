# Append method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

for element in stu_roll:
    print(element)

print("-"*5)
print("After appending a new element")

stu_roll.append(106)

for element in stu_roll:
    print(element)
