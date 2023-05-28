# Set Comprehension

set1 = set()

for i in range(20):
    set1.add(i + 1)

print("without using comprehension:", set1)


set2 = {i + 1 for i in range(20)}
print("Using Comprehension:", set2)

print()

# creating a set of even numbers in a given range
set3 = {i for i in range(21) if i % 2 == 0}
print("Even Set:", set3)

print()

# creating a set of numbers divisible by 2 and 3
set4 = {i for i in range(21) if i % 2 == 0 if i % 3 == 0}
print("divisible by 2 and 3:", set4)

print()

# set comprehension using if else
set5 = {i if i % 2 == 0 else i * 100 for i in range(21)}
print("using if else in comprehensions:", set5)
