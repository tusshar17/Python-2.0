# Abstract Class

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass

    def show(self):
        print("Concrete Method")


class Son(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")


# c = Father() -->TypeError: Can't instantiate abstract class Father with abstract methods disp

c = Son()
c.disp()
c.show()