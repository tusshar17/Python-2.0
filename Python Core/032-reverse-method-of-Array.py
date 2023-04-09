# reverse method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

for element in stu_roll:
    print(element)

# reverse the array
stu_roll.reverse()

print("After reversing the array")
for element in stu_roll:
    print(element)
