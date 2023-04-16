# Creating Numpy 2D array from user input

import numpy as np
m = int(input("Enter Number of Rows: "))
n = int(input("Enter Number of Columns: "))

a = np.zeros((m, n), dtype=int)

for i in range(m):
    for j in range(n):
        a[i][j] = int(input("Enter element in "+str(i) +
                            " row at "+str(j)+" column: "))


for r in a:
    for c in r:
        print(c, end=" ")
    print()
