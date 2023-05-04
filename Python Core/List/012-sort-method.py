# sort() method

a = [30, 10, 40, 20, 50]

print("before sorting:", a)

a.sort()

print("after sorting:", a)


b = [30, 10, 40, 20, 50, 'hello']
# b.sort()  --> TypeError: '<' not supported between instances of 'str' and 'int'

#
c = ['a', 'b', 'e', 'd', 'c']
print(c.sort())
