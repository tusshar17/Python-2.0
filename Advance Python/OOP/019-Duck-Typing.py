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


def fun(obj):
    obj.speak()

d = Duck()
fun(d)

c = Cat()
fun(c)

s = Snail()
fun(s) #--> AttributeError: 'Snail' object has no attribute 'speak'