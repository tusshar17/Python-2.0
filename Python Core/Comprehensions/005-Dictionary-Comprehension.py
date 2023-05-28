# Dictionary COmprehension

dict1 = {i: i**2 for i in range(11)}
print(dict1)

# with one if condition
dict2 = {i: i**2 for i in range(11) if i % 2 == 0}
print(dict2)

# with if else
dict3 = {n: "even" if n % 2 == 0 else "odd" for n in range(11)}
print(dict3)

print()

# list of tuples to dictionary
lst = [(1, "tushar"), (2, "rahul"), (3, "simran")]
dict4 = {k: v for k, v in lst}
print(dict4)
