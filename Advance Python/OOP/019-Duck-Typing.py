# Duck Typing

class Duck:
    def speak(self):
        print("quack quack...")


class Cat:
    def speak(self):
        print("meow meow...")

class Snail:
    def walk(self):
        print("crawl.....")


d = Duck()
d.speak()

c = Cat()
c.speak()

s = Snail()
# s.speak() --> AttributeError: 'Snail' object has no attribute 'speak'