# global keyword

a = "global"


def show():
    a = "local"
    print("A inside function:", a)


show()

print("A outside function:", a)

print("\n")


#
i = 0


def show2():
    global i
    i = i+1
    print("i inside function", i)


show2()
print("i outside function", i)
