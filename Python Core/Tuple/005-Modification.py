# Modification in Tuples

a = 1, 2, 3, 4, 5

# a[1] = 99  --> TypeError: 'tuple' object does not support item assignment

c = a + (6, 7)
print(c)

print()

# insert 99 at 2nd index
print("before:", a)
res = a[0:2] + (99,) + a[2:]
print("after:", res)
# although original tuple remains unchanged
