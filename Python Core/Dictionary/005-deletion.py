# deletion in dictionary

students = {101: "raj", 102: "rahul", 103: "sonam"}

print("Original Dictionary:", students)

# deleting an item
del students[102]

print("After Deleting 102:", students)

# deleting complete dictionary
del students

# print(id(students)) --> NameError: name 'students' is not defined
