# ===== Nestedf If Else Statements=====

a = 5
b = 10

if a > b:
    print("a is greater than b")
    if a % 2 == 0:
        print("a is even too")
    else:
        print("a is not even")

else:
    print("b is greater than a")
    if b % 2 == 0:
        print("b is even too")
    else:
        print("b is not even")
