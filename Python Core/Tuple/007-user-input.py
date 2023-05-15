# Creating a tuple from user input

a = []

n = int(input("Enter number of elements: "))

for i in range(n):
    a.append(int(input("Enter " + str(i) + " element: ")))

tpl = tuple(a)
print(tpl, type(tpl))


# since tuples are immutable, take user input in list and typecast that into tuple
