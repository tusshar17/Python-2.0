# copy method

students = {101: "raj", 102: "rahul", 103: "sonam"}
print("original Dictionary:")
print(students)
print(id(students))
print()

new_students = students.copy()
print("Copied Dictionary:")
print(new_students)
print(id(new_students))
print()
