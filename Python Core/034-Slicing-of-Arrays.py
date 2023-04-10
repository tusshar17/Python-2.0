# ===== Slicing of Arrays =====

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105, 106, 107, 108, 109, 110])

print("Original Array:")
for i in range(len(stu_roll)):
    print(i, ":", stu_roll[i])

print("-"*5)

a = stu_roll[0:5]
for element in a:
    print(element, end=" ")

print("\n", "-"*5)

b = stu_roll[5:]
for element in b:
    print(element, end=" ")

print("\n", "-"*5)

c = stu_roll[2:8:3]
for element in c:
    print(element, end=" ")

print("\n", "-"*5)

d = stu_roll[::-1]
for element in d:
    print(element, end=" ")

print("\n", "-"*5)

e = stu_roll[-10:-5]
for element in e:
    print(element, end=" ")
