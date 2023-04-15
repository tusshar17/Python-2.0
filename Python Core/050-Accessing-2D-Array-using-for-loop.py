# Accessing 2D Array using for loop

import numpy as np

a = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80]
])

# without index

for r in a:
    for c in r:
        print(c, end=" ")
    print()


print("-"*5)


# with index

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
