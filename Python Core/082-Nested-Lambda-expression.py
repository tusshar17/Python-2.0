# nested lambda exoression

# add = lambda x=10: (lambda y: x+y)
def add(x=10): return (lambda y: x+y)


a = add()

print(a(20))
print(a)
