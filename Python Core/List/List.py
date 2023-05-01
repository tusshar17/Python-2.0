# List

a = [10, 20, -50, 21.3, 'Hello']

print(a)

# accessing elements using index
print("0:", a[0])
print("1:", a[1])
print("2:", a[2])
print("-1:", a[-1])

print()

# modifying elements
print("list before modification:", a)
print("list id before modification:", id(a))
a[1] = 40
print("list after modification:", a)
print("list id after modification:", id(a))
