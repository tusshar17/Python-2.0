a = 10
print(a)

print(id(a))

b = 10

print(id(b))

"""

id(a) is equal to id(b) since value of a is equal to b
and in python variable do not have access of memory address unlike 
other programming languages such as C, C++ or Java

"""

""" let's try to change the value of a """

a = 20
print(a)
print(id(a))


""" 
value of id(a) changed since value of a is changed 
a points to an object which is stored at a particular address

In other programming languages, variables are assigned a partcular 
memory space. when we change the value of that variable it do not change
memory address, it changes the value stored

while in Python, when we change the value of a variable
it refers to another memory address storing that value.
and the previous value is removed by garbage collector (if unused) 

"""

"""
if we store value of a in c
"""

c = a
print("id of a: ", id(a))
print("id of c: ", id(c))

"""
id(a) is equal to id(c) since value of a and c are same 
"""
