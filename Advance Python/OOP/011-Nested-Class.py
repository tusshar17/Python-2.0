# Nested Class


class Team:  # outer class
    def __init__(self) -> None:
        self.name = "Joy"
        self.device = self.Device()  # creating inner class object

    def show(self):
        print("Name:", self.name)

    class Device:  # inner class
        def __init__(self) -> None:
            self.name = "Laptop"
            self.price = 500000

        def display(self):
            print("Devic Name:", self.name)
            print("Devic Price:", self.price)


a = Team()
# print(a.name)
a.show()

# print(a.device.name)
a.device.display()
