# accessing nested dict using loop

a = {"course": "Python", "fees": 15000, 1: {"course": "Javascript", "fees": 10000}}

print("original dict:", a)

for key in a:
    if type(a[key]) is dict:
        for key2 in a[key]:
            print(key, key2, ":", a[key][key2])
    else:
        print(key, ":", a[key])
