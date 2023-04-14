# creating a numpy array from user input

from numpy import *

n = int(input("Enter the size of array: "))

arr = zeros(n, dtype=int)

for i in range(n):
    arr[i] = int(input("Enter "+str(i)+" element: "))

for element in arr:
    print(element)
