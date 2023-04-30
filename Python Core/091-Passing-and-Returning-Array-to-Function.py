# Passing Array to Function

from array import *


def show(arr):
    print(arr)
    print(type(arr))
    for i in arr:
        print(i)


arr = array('i', [10, 20, 30])
show(arr)

print()


# Returning Array from Function


def myfun():
    a = array('i', [1, 2, 3])
    print("inside:", id(a))
    return a


ar = myfun()
print(ar)
print(type(ar))
print("outside:", id(ar))
ar.append(4)
print(ar)
