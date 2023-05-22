# setdefault() method

students = {101: "raj", 102: "rahul", 103: "sonam"}
print("original dictionary:", students)
print()

new_added_item = students.setdefault(104, "joy")
print("after setdefault dictionary:", students)
print()
print("new added element:", new_added_item)
