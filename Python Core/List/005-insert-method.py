# insert() method

a = [10, 20, 30, 40, 50]

print("Before:", a)

a.insert(3, 99)

print("After:", a)

# special case : inserting element at an index out of length of list, it will be added at last
a.insert(100, 11)
print(a)
