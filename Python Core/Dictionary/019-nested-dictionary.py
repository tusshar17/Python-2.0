# nested dictionary

# empty nested dictionary

a = {1: {}, 2: {}, 3: {}}

print(a)
print(type(a))
print()

#

a = {"course": "Python", "fees": 15000, 1: {"course": "Javascript", "fees": 10000}}
print(a)
print(type(a))

print(a["course"])
print(a["fees"])

print(a[1]["course"])
print(a[1]["fees"])

print()

# modifying
a["course"] = a["course"] + " (Django)"
print("after modification:", a)

print()

# adding one more nested dict
a[2] = {"course": "Rust", "fees": 16000}
print("after adding one more nested dict:", a)
