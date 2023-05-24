# accessing dictionary using loop

students = {101: "raj", 102: "rahul", 103: "sonam"}
print("original dictionary:", students)
print()

for key in students:
    print(key, ":", students[key])
