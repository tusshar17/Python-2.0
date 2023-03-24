# ===== In Built Dataypes =====


# ----- Numeric Type -----

# Int
y = 10
print(y)
print(type(y))


# Float
price = 25.56
print(price)
print(type(price))


# Complex Number
com = 5 + 7j
print(com)
print(type(com))


# Boolean
yes = True
no = False
print(yes)
print(type(yes))

res = yes + no
print(res)
print(type(res))


# ----- Sequence Type -----

# String
str1 = "Hello World"
print(str1)
print(type(str1))

# List
data = [10, 20, -50, 21.3, 'HelloWorld']
print(data)
print(type(data))

print(data[0])
print(data[-1])

data[0] = 100
print(data)

# Tuple
data2 = (10, 20, -50, 21.3, 'HelloWorld')
print(data2)
print(type(data2))

print(data2[0])
print(data2[-1])

''' 
data2[0] = 100   
Error --> TypeError: 'tuple' object does not support item assignment 
 '''

# Range
rg = range(5)
print(rg)
print(rg[0])
print(type(rg))

rg2 = range(10, 20, 2)
print(rg2[0])
print(rg2[1])
print(rg2[-1])


# ----- Set Type -----

dataSet = {10, 20, 30, "HelloWorld", "DEV", 40}
print(dataSet)
print(type(dataSet))

'''
print(dataSet[0])
Error --> TypeError: 'set' object is not subscriptable
'''

dataSet2 = {10, 20, 30, 10, 20}
print(dataSet2)


# ----- Map/dict/Dictionary Type -----

dataDict = {101: 'Rahul', 102: 'Raj', 103: 'Sonam'}
print(dataDict)
print(type(dataDict))

print(dataDict[101])
