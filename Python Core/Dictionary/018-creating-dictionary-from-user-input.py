# creating dictionary using user input

a = {}

n = int(input("Enter number of elements: "))

for i in range(n):
    key = input("Enter key for " + str(i) + " element: ")
    value = input("Enter value of " + str(i) + " element: ")

    a.update({key: value})


print(a)
