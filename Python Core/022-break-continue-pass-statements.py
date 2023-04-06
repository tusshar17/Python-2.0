# ===== break, continue and pass statements =====


# break

# a program to print each character of a string and stop printing when 'x' comes

st = "HelloxWorld"

for ch in st:
    print(ch)
    if ch == 'x':
        break


print("-"*5)


# continue

# a program to print each character of a string except vowels

st = "HelloWorld"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for ch in st:
    if ch in vowels:
        continue
    print(ch)

print("-"*5)


# pass - do nothing

# a program to print each vowel of a string

st = "HelloWorld"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for ch in st:
    if ch not in vowels:
        pass
    else:
        print(ch)
