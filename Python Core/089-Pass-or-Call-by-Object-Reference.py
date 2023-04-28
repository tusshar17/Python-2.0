# Pass or Call by Object Reference

def val(x):
    print(x, id(x))
    x = 15
    print(x, id(x))


x = 10
val(x)
print(x, id(x))

print("\n")


# modifying object
def myfun(lst):
    print("Inside Function Before Append:", lst, id(lst))
    lst.append(4)
    print("Inside Function After Append:", lst, id(lst))


lst = [1, 2, 3]
print("Before Calling Function:", lst, id(lst))
myfun(lst)
print("After Calling Function:", lst, id(lst))

print("\n")


# creating a new object
def myfun2(lst):
    print("Inside Function Before:", lst, id(lst))
    lst = [11, 22, 33]
    print("Inside Function After:", lst, id(lst))


lst = [1, 2, 3]
print("Before Calling Function:", lst, id(lst))
myfun2(lst)
print("After Calling Function:", lst, id(lst))
