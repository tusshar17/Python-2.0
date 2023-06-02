# Example 1
print("====Example 1====")


class MyClass:
    def say_hello(self):
        print("Hello World")


x = MyClass()
x.say_hello()

print(x)
print(x.say_hello)

print()


# Example 2
print("====Example 2====")


class Mobile:
    def __init__(self):
        self.model = "Samsung A51"

    def show_model(self):
        print("Model:", self.model)


samsung = Mobile()
samsung.show_model()

# modifying model
samsung.model = "Samsung S23"
print("After modifying model:")
samsung.show_model()


print()


# Example 3 --> constructor with argument
print("====Example 3====")


class Mobile2:
    def __init__(self, m):
        self.model = m

    def show_model(self, p):
        print("Model:", self.model, "\nPrice:", p)


apple = Mobile2("iphone 12")
apple.show_model(80000)

print()

samsung = Mobile2("A51")
samsung.show_model(23000)

print()

print("apple ->", apple)
print("samsung ->", samsung)
