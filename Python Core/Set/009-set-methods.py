# set methods

a = {"a", "b", "c", "d"}
b = {"c", "d", "e", "f"}

print("a:", a)
print("b:", b)

print()

# intersection
i = a.intersection(b)
print("a intersection b:", i)


# union
u = a.union(b)
print("a union b:", u)


# difference
d = a.difference(b)
print("a difference b:", d)

d1 = b.difference(a)
print("b difference a:", d1)


# issubset
subset = a.issubset(b)
print("a is subset of b:", subset)


# issuperset
superset = a.issuperset(b)
print("a is superset of b:", superset)
