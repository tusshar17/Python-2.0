# Passing/Returning Dict to/from function


def fun(d):
    # add a new element
    d["new"] = "new element"
    return d


a = {1: "a", 2: "b", 3: "c"}
print("original:", a)

print("after function:", fun(a))
