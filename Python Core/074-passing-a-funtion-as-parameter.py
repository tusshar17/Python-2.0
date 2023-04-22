# Passing a function as parameter

def display(sh):
    print("Display Function "+sh())


def show():
    return "Show Function"


display(show)
