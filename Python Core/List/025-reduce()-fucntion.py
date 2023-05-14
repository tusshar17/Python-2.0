# reduce() function

from functools import reduce

x = [10, 20, 30, 40, 50]

res = reduce(lambda a, b: a + b, x)

print(res)
print(type(res))
