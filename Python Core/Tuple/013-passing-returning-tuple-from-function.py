# Passing/Returning Tuple to/from Function


# a function which accepts a tuple as parameter and returns a tuple having double elements of that


def double_elem(tpl):
    res = tpl[0:] + tpl[0:]
    return res


a = 1, 2, 3, 4, 5
print(double_elem(a))
