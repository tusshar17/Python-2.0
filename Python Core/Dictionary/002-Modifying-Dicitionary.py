# Modifying Dictionary

students = {101: "raj", 102: "rahul", 103: "sonam"}
print("Before modification:", students)
print(id(students))
print()

students[102] = "Jay"

print("After modification:", students)
print(id(students))
