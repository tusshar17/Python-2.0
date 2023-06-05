# Instance Method


# Instance Method without Parameter
class Mobile:
    # Insatance Method
    def show_model(self):
        print("Iphone 12")


apple = Mobile()
apple.show_model()


# Instance Method with Parameter
class Mobile2:
    def __init__(self):
        self.model = "Iphone 12"  # Instance Variable

    def show_model(self, p):
        self.price = p
        print("Model:", self.model, "Price:", self.price)


apple2 = Mobile2()
apple2.show_model(100000)
