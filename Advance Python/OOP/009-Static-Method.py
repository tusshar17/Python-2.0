# Static Method


# without parameter
class Mobile:
    fp = "yes"

    @staticmethod
    def show_model():
        print("Iphone 12")
        print("Fingerprint:", Mobile.fp)


apple = Mobile()
Mobile.show_model()

print()


# with parameter
class Mobile2:
    @staticmethod
    def show_model(m, p):
        model = m
        price = p
        print("Model:", model)
        print("Price:", price)


apple2 = Mobile2()
Mobile2.show_model("Iphone 13", 120000)
