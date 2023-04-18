# Memory Allocation in Strings

str1 = "HelloWorld"
str2 = "HelloWorld"
str3 = "Python"

print("Value of str1:", str1)
print("Value of str2:", str2)
print("Value of str3:", str3)
print()
print("Address/id of str1:", id(str1))
print("Address/id of str2:", id(str2))
print("Address/id of str3:", id(str3))

print("-"*15)

str4 = "Programming"
print("(Before) Value of str4:", str4)
print("(Before) id of str4:", id(str4))

str4 = "Coding"
print("(After) Value of str4:", str4)
print("(After) id of str4:", id(str4))
