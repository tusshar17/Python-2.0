# Deleting Elements from Set

a = {1, 2, 3, "hello"}

print("Original Set:", a)

a.remove("hello")
print("After removing 'hello':", a)

# a.remove("hello") --> KeyError: 'hello'

a.discard(1)
print("After discarding 1:", a)
