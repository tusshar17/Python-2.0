# ===== Logical Operators =====


# Logical and
a = 5
b = 2
c = 3
d = 1

print(a > b and a > c)
print(a > b and a < c)

# True and Exp1 -> Exp1
print(a > b and c)
# True and Exp1 and Exp2 -> Exp2
print(a > b and c and d)

# False and Exp1 -> False
print(a < b and b)
# False and Exp1 and Exp2 -> False
print(a < b and b and c)


# Logical or

print(a > b or a > c)
print(a > b or a < c)
print(a < b or a < c)

# True or Exp1 -> True
print(a > b or c)
# True or Exp1 or Exp2 -> True
print(a > b or c or d)

# False or Exp1 -> Exp1
print(a < b or b)
# False or Exp1 or Exp2 -> Exp1
print(a < b or b or c)


# Logical not
a = 5
b = 2

print(not(a > b))
