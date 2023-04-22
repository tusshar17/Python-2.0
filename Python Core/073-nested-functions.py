# Nested functions

def display():
    def show():
        print("show function")
    print("display function")
    show()


display()


def printName(fname, lname):

    def printFname():
        return fname

    def printLname():
        return lname

    res = "My first name is : "+printFname()+" and last name is : "+printLname()

    return res


print(printName("Tushar", "Kumar"))
