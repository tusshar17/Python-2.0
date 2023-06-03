# Instance Variable


class Hello:
    # consructor
    def __init__(self):
        self.var = "This is an Instance Varable"

    # instance method
    def show(self):
        print(self.var)  # accessing instance variable inside a instance method


obj1 = Hello()
print("obj1.var:", obj1.var)  # accesing instance variable outside the class

obj2 = Hello()
print("obj2.var:", obj1.var)  # accesing instance variable outside the class

print()

# modifying instance variables
obj1.var = obj1.var + " of obj1"
obj2.var = obj2.var + " of obj2"

print("After Modification:")
print("obj1.var:", obj1.var)
print("obj2.var:", obj2.var)
