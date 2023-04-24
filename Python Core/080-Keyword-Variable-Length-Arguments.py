# Keyword Variable Length Arguments

def add(**num):
    z = num['a']+num['b']+num['c']
    print(z)


add(a=5, b=10, c=15)
