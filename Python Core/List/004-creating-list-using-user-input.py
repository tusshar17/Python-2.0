# Creating List using User Input

a = []

n = int(input("How mant elements to add : "))

for i in range(n):
    a.append(input("Enter "+str(i)+" element: "))

print(a)
