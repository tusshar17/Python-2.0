# Accessing String using Loop

str1 = "HelloWorld"

# without index
for c in str1:
    print(c)

print("-"*15)

# with index
for i in range(len(str1)):
    print("str1["+str(i)+"] :", str1[i])
