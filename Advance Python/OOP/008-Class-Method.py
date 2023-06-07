# Class Method


# without parameter
class Mobile:
    fp = "yes"

    @classmethod
    def show_model(cls):
        print("Model: Iphone 12", "\nFingerprint:", cls.fp)


apple = Mobile()
Mobile.show_model()

print()


# with parameter
class Mobile2:
    fp = "yes"

    @classmethod
    def show_model(cls, r):
        print("Fingerprint:", cls.fp)
        cls.ram = r
        print("RAM:", cls.ram)


apple2 = Mobile2()
Mobile2.show_model("8GB")
