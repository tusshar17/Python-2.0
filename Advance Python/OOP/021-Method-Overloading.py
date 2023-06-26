# Method Overloading

class MyClass:
    def sum(self, a=None, b=None, c=None):
        
        if b==None and c==None:
            s = "provide atleast 2 arguments!"
        elif c==None:
            s = a+b
        else:
            s = a+b+c
        
        return s
    

obj = MyClass()
print(obj.sum())
print(obj.sum(10))
print(obj.sum(10, 20))
print(obj.sum(10, 20, 30))