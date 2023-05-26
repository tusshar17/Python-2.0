# List Comprehensions

lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

new_lst1 = []

for i in lst1:
    new_lst1.append(i + 1)

print("lst1:", lst1)
print("new_lst1:", new_lst1)


# using list comprehension

new_lst2 = [i + 1 for i in lst1]
print("new_lst2:", new_lst2)

print()

new_lst3 = [i + 1 for i in range(20)]
print("new_lst3:", new_lst3)

print()

# ====creating a list which stores even number in a given range====

# without using comprehension

even_lst = []

for i in range(20):
    if i % 2 == 0:
        even_lst.append(i)

print("even_lst:", even_lst)

# using comprehension

even_lst2 = [i for i in range(20) if i % 2 == 0]
print("even_lst2:", even_lst2)

print()


# ====creating a list which stores numbers divisible by both 2 & 3 in a given range====

# without using comprehension

list23 = []

for i in range(20):
    if i % 2 == 0 and i % 3 == 0:
        list23.append(i)

print("list23:", list23)

# using comprehension

list23 = [i for i in range(20) if i % 2 == 0 if i % 3 == 0]
print("list23:", list23)

print()


# ====list comprehension using if else====

a = []

for i in range(20):
    if i % 2 == 0:
        a.append(i)
    else:
        a.append("invalid")

print(a)

a1 = [i if i % 2 == 0 else "invalid" for i in range(10)]
print("using list comprehension with if else:", a1)
