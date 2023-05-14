# map() function


def after_10_yrs(age):
    return age + 10


people_age = [12, 34, 63, 22, 15, 23, 26]
print("Current Age:", people_age)
print("After 10 Years:", list(map(after_10_yrs, people_age)))

print()

# perfoming map using multiple sequeces

a = [10, 20, 30, 40, 50]
b = [1, 2, 3, 4, 5]

print(list(map(lambda a, b: a + b, a, b)))
