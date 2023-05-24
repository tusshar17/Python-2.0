# setdefault() method

students = {101: "raj", 102: "rahul", 103: "sonam"}
print("original dictionary:", students)
print()


# if key exists
returned_value = students.setdefault(102, "default")
print(returned_value)


# if key do not exists
returned_value = students.setdefault(109, "default")
print(returned_value)
print()

print("dictionary after setdefault() :", students)
