# Accessing Array elements using for loop
from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

# without using index
for element in stu_roll:
    print(element)

print("-"*5)

# using index
n = len(stu_roll)  # return length of array (no. of elements)

for i in range(n):
    print(stu_roll[i])

print("-"*5)

# printing array elements along with index number
for i in range(n):
    print("At index", i, ":", stu_roll[i])
