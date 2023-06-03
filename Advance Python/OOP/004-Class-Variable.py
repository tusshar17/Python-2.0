# Class/Static Variable


class Hello:
    class_var = "This is a class variable"  # class variable

    def __init__(self):
        self.var = "This is a instance variable"  # instance variable

    def show(self):  # instance method
        print(self.var)  # accessing instance variable inside instance method

    @classmethod
    def class_method(cls):
        # accessing class variable inside class method
        print("Inside Class Method:", cls.class_var)


obj1 = Hello()
obj1.show()  # calling instance method

obj2 = Hello()
obj2.show()

Hello.class_method()  # calling class method

# modifying class variable
# accessing class variable outside the class
Hello.class_var = "class variable modified"
Hello.class_method()
