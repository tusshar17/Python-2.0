# insert method of array class

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

for element in stu_roll:
    print(element)


# insert 100 at index 3
stu_roll.insert(3, 100)

print("after inserting 100 at index 3")

for element in stu_roll:
    print(element)
