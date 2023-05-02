# pop() method

a = [10, 20, 30, 40, 50]

print("Before pop() :", a)

a.pop()

print("After pop() :", a)

# pop(n)

print("Removed element :", a.pop(1))
print("After pop(1) :", a)

# print(a.pop(55))  -->IndexError: pop index out of range
