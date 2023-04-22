# Return Statements

# Returning a single value
def add(x, y):
    sum = x+y
    return sum


res = add(10, 20)
print(res)

# Returning multiple values
def add_sub(x, y):
    add = x+y
    sub = x-y
    return add, sub

sum, sub = add_sub(15, 10)
print(sum)
print(sub)