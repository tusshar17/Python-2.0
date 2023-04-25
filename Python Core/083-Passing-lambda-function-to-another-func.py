# passing lambda function to another function

def show(a):
    print(a(8))


show(lambda x: x**2)


# returning lambda function from a function

def add():
    y = 100
    return lambda x: x+y


a = add()
print(a(10))
