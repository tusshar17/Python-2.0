# Keyword Arguments

def show(name, age):
    print("My name is {} and my age is {}".format(name, age))


show(name="Rahul", age=15)

show(age=15, name="Rahul")

# show(name="Rahul", age=15, roll=101) --> TypeError: show() got an unexpected keyword argument 'roll'
print()
show("Rahul", 15)
show(15, "Rahul")
