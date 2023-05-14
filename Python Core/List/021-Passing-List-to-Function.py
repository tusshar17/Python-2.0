# Passing and returning List to/from Function


# passing
def fun(lst):
    print("Type of parameter:", type(lst))
    print(lst)


a = [1, 2, 3, 4, 5]
fun(a)

print()

# passing and rerturning


def double_elem(lst):
    res = lst * 2
    res.sort()
    return res


x = [1, 2, 3]
print("Original List:", x)

print("Doubled Elements:", double_elem(x))
