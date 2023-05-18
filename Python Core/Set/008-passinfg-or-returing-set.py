# passing/returning set to/from function


# function which accepts a set as parameter and retruns a set
def fun(s):
    s.add("new-element")
    return s


a = {1, 2, 3, 4, 5}
print(fun(a))
