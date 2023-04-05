# ===== While Loop =====

a = 1

while a <= 10:
    print(a)
    a += 1

print("Rest of the code")


# While else loop

a = 1

while a <= 5:
    print(a)
    a += 1
else:
    print("Else part of the loop")

print("rest of the code")


# Infinite while loop

# while True:
# print("Hello World")

i = 1

while True:
    print(i)
    i += 1
    if i > 5:
        break

# Nested while loop
i = 1
while i <= 3:
    print("outer loop", i)
    i += 1
    j = 1
    while j <= 3:
        print("inner loop", j)
        j += 1
print("rest of the code")
