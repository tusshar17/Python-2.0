# Craeting Tuples

# empty tuple
a = ()
print(a, type(a))

# with one element
b = 10
print(b, type(b))

c = (10,)
print(c, type(c))


# with multiple elements
d = (10, 20, -50, 21.3, "hello")
print(d, type(d))

e = 0, 20, -50, 21.3, "hello"
print(e, type(e))

# accessing elements using index
print(d[0])
print(d[-1])
print(d[-2])


# trying to modify elements
# d[0] = 99   --> TypeError: 'tuple' object does not support item assignment
