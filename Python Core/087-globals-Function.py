# globals() function

a = 10


def show():
    b = 20


print(globals())
print(globals()['a'])

print("\n")


#
i = 5


def myfun():
    x = globals()['i']+2
    print('x:', x)


print('i:', i)
myfun()
