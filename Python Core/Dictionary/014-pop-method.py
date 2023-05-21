# pop() method

students = {101: "raj", 102: "rahul", 103: "sonam"}

print("orginal dictionary:", students)

student_who_left = students.pop(102)
print(student_who_left, "left the school.")

print("after:", students)


# print(students.pop(109))  -->KeyError: 109

print(students.pop(109, "no such student"))
