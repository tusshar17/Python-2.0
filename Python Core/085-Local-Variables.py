# Local Variables

def show():
    name = "Rahul"
    print("Hello", name)


show()

# print(name) --> NameError: name 'name' is not defined
print("\n")

# Global Variables

a = "Global Variable"


def show2():
    x = "Local Variable"
    print(a, "inside function")
    print(x, "inside function")


show2()
# print(x, "outside function") --> NameError: name 'x' is not defined
print(a, "outside function")

print("\n")
# special case
i = 1


def myfun():
    # i = i + 1   --> UnboundLocalError: local variable 'i' referenced before assignment
    print(i)


myfun()
