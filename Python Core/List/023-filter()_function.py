# filter() function


def can_vote(age):
    if age >= 18:
        return True


people_ages = [23, 13, 64, 22, 17, 19]

result = filter(can_vote, people_ages)

print(result)
print(type(result))

for x in result:
    print(x)

print()

# using lamba

result2 = filter(lambda n: n >= 18, people_ages)
print(list(result2))

# if passed function is none
a = [1, 0, 1, 1, 0, 0]
print(list(filter(None, a)))
