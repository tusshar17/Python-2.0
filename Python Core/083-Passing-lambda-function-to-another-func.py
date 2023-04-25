# passing lambda function to another function

def show(a):
    print(a(8))


show(lambda x: x**2)
