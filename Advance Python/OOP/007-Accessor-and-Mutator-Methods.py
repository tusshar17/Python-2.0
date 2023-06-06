# Accesor and Mutator Method


# Accessor or getter method
class Mobile:
    def __init__(self):
        self.model = "Iphone 12"

    def get_model(self):
        return self.model


apple = Mobile()
print(apple.get_model())


# Mutator or setter method
class Mobile2:
    def set_model(self, m):
        self.model = m


apple2 = Mobile2()
apple2.set_model("Iphone 13")
print(apple2.model)
