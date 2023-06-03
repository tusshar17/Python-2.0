# Constructor

# without parameter


class Speak:
    def __init__(self):
        self.message = "Hello!"
        print(self.message)


obj = Speak()


# with parameter
class SpeakName:
    def __init__(self, name):
        self.message = "Hello! " + name
        print(self.message)


obj2 = SpeakName("World")
obj = SpeakName("Joy")
