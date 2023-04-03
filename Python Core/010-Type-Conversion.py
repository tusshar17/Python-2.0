# ===== Type Conversion =====


# Implicit Type Conversion

a = 5
b = 2
value = a/b
print(value)
print(type(value))

x = 10
y = 5.5
res = x+y
print(res)
print(type(res))


# Explicit Type COnversion

'''
s1 = 'Hello'     # type -> str
s2 = 99          # type -> int
s3 = s1+s2

will generate error --> TypeError: can only concatenate str (not "int") to str

'''

a = 5
b = 2
value = a/b
print(value)
print(type(value))

int_value = int(value)
print(int_value)
print(type(int_value))


s1 = 'Hello'
s2 = 99
s3 = s1+str(s2)
print(s3)
print(type(s3))

# Float to Integer
float_n = 9.9
int_n = int(float_n)
print(int_n)
print(type(int_n))

# Integer to Float
int_n = 10
float_n = float(int_n)
print(float_n)
print(type(float_n))

# Int to Complex
int_n = 10
complex_n = complex(int_n)
print(complex_n)
print(type(complex_n))

# String to Tuple
s1 = "hello"
tuple_s1 = tuple(s1)
print(tuple_s1)
print(type(tuple_s1))

# String to List
s1 = "hello"
list_s1 = list(s1)
print(list_s1)
print(type(list_s1))

# List to Tuple
lst = [1, 2, 3]
tpl = tuple(lst)
print(tpl)
print(type(tpl))

# Tuple to List
tpl = (1, 2, 3)
lst = list(tpl)
print(lst)
print(type(lst))

# Decimal to Binary
decimal = 10
binary = bin(decimal)
print(binary)
print(type(binary))
