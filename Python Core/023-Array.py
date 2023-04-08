# ===== Array =====


# import array

# method 1
'''
import array as ar

stu_roll = ar.array('i', [101, 102, 103, 104, 105])

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])
'''

# method 2

from array import *

stu_roll = array('i', [101, 102, 103, 104, 105])

print(stu_roll[0])
print(stu_roll[1])
print(stu_roll[2])
print(stu_roll[3])
print(stu_roll[4])


price = array('f', [10.5, 20.2, 15])

print(price[0])
print(price[1])  # something different
print(price[2])
