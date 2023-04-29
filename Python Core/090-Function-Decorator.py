# Function Decorator

def decor(fun):
    def inner():
        print("Inner Function: Before Enhancing")
        fun()
        print("Inner Function: After Enhancing")
    return inner


@decor
def show():
    print("Inside Function")


show()

# num = decor(num)
# num()
#

print()


#
def decor2(num):
    def inner():
        a = num()
        return a+5
    return inner


@decor2
def num():
    return 10


print(num())

# result_fun = decor2(num)
# print(result_fun())


#
def decorA(myfun):
    def inner():
        a = myfun()
        add = a+5
        return add
    return inner


def decorB(myfun):
    def inner():
        b = myfun()
        multiply = b*10
        return multiply
    return inner


@decorA
@decorB
def myfun():
    return 10


print(myfun())
# res = decorB(decorA(myfun))
# print(res())


@decorB
@decorA
def myfun():
    return 10


print(myfun())
# res = decorA(decorB(myfun))
# print(res())
