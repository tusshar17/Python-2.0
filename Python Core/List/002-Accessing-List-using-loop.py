# Accessing List using loops

a = [10, 20, -50, 21.3, 'Hello']

# without using index
for element in a:
    print(element)

print()

# using index
for i in range(len(a)):
    print(i, ":", a[i])

print()

i = 0
while i < len(a):
    print(i, ":", a[i])
    i += 1
