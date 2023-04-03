# ===== If-Elif-Else Statements=====

# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))

# if a > b:
#     print(a, "is greater than", b)
# elif a < b:
#     print(a, "is less than", b)
# elif a == b:
#     print(a, "is equal to", b)


teamA = ["a", "b", "c"]
teamB = ["d", "e", "f"]

player = input("Enter player name: ")

if player in teamA:
    print(player, "belongs to Team 'A'")
elif player in teamB:
    print(player, "belongs to Team 'B'")
else:
    print("no such player")
