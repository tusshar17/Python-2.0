# update() method

students = {101: "raj", 102: "rahul", 103: "sonam"}

print("original dictionary:", students)

# adding single key value pair
students.update({104: "karan"})
print("after adding one more element:", students)

# adding multiple key value pairs
a = {105: "ram", 106: "lucky", 107: "sameer", 108: "joy"}
students.update(a)
print("after adding few more values:", students)
