# pop method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

for element in stu_roll:
    print(element)


stu_roll.pop()

print("after using pop()")

for element in stu_roll:
    print(element)


# pop(position)

# remove the element from index 2
r = stu_roll.pop(2)
print("after using pop(2)")

for element in stu_roll:
    print(element)

print("Removed Element:", r)
