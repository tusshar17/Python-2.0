# get() method

students = {101: "raj", 102: "rahul", 103: "sonam"}

print("Original Dictionary:", students)
print()

print(students.get(101))
print(students.get(104))
print(students.get(104, "default"))
