# Nested Lis Comprehension

a = []

for i in range(1, 6):
    a.append([])
    for j in range(1, 6):
        a[i - 1].append([])
        a[i - 1][j - 1] = i * j

print("without using comprehension:", a)

b = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("Using Comprehension:", b)
