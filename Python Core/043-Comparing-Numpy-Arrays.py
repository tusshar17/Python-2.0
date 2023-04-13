# Comparing Numpy Arrays using Relational Operators

from numpy import *

a = array([100, 200, 300, 400, 500])
b = array([100, 20, 30, 400, 50])

result = a == b
print("result :", result)

result2 = a < b
print("result2 :", result2)


# any() function
print("any(result) :", any(result))

# all() function
print("all(result) :", all(result))
