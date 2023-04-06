# ===== for Loop =====

st = "Hello Wolrd"

for ch in st:
    print(ch)

print("rest of the code")


# for loop using range() function
for i in range(5):
    print(i)

print("-"*5)

for i in range(1, 5):
    print(i)

print("-"*5)

for i in range(1, 10, 2):
    print(i)

print("-"*5)


st = "HelloWorld"
st_length = len(st)

for i in range(st_length):
    print(i, ":", st[i])

print("-"*5)


# for loop with else

for i in range(0, 10, 2):
    print(i)
else:
    print("else part")


# nested for loop

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()
