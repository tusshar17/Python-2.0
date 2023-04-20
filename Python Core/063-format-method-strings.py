# format() method


# integer
print("{}".format(10))
print("{} {}".format(10, 20))
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10, num2=20))
print("{num2} {num1}".format(num1=10, num2=20))
print()


# float
print("{}".format(10.56))
print("{} {}".format(10.56, 20.42))
print("{0} {1}".format(10.56, 20.42))
print("{1} {0}".format(10.56, 20.42))
print("{num1}".format(num1=10.56))
print("{num1} {num2}".format(num1=10.56, num2=20.42))
print("{num2} {num1}".format(num1=10.56, num2=20.42))
print()


# string
print("{}".format("Hello"))
print("{} {}".format("Hello", "World"))
print("{0} {1}".format("Hello", "World"))
print("{1} {0}".format("Hello", "World"))
print("{str1}".format(str1="Hello"))
print("{str1} {str2}".format(str1="Hello", str2="World"))
print("{str2} {str1}".format(str1="Hello", str2="World"))
print()


# integer with type specifier
print("{}".format(15))
print("{:d}".format(15))
print("{0:d}".format(15))
print("{num:d}".format(num=15))
print()

# using fill and alignment
print("{num:5d}".format(num=15))
print("{num:05d}".format(num=15))
print("{num:+5d}".format(num=15))
print("{num:<5d}".format(num=15))
print("{num:*<5d}".format(num=15))
print("{num:*>5d}".format(num=15))
print("{num:*^5d}".format(num=15))
print()

# for string
print("{:8s}".format("Hello"))
print("{:<8s}".format("Hello"))
print("{:*<8s}".format("Hello"))
print("{:>8s}".format("Hello"))
print("{:*>8s}".format("Hello"))
print("{:^8s}".format("Hello"))
print("{:*^8s}".format("Hello"))
print()

print("using precision")

print("{:8.3s}".format("Hello"))
print("{:<8.3s}".format("Hello"))
print("{:*<8.3s}".format("Hello"))
print("{:>8.3s}".format("Hello"))
print("{:*>8.3s}".format("Hello"))
print("{:^8.3s}".format("Hello"))
print("{:*^8.3s}".format("Hello"))
print()
print()

print("{:,}".format(1234567890))
print("{:_}".format(1234567890))

print()
print("using variables")

name = "Rahul"
age = 15
print("My name is {}. My age is {}.".format(name, age))
