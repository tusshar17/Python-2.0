# adding element from user input

a = set()

n = int(input("Enter no. of elements: "))

for i in range(n):
    a.add(input("Enter " + str(i) + " element: "))

print(a)
