# Getting Input from user

from array import *

stu_roll = array('i', [])
n = int(input("How many elements to be added: "))

for i in range(n):
    stu_roll.append(int(input("Enter element: ")))

for i in range(n):
    print(stu_roll[i])
