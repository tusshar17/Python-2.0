# Recursion


# i = 1


# def myfun():
#     global i
#     print("HelloWorld:", i)
#     i += 1
#     myfun()


# myfun()

# RecursionError: maximum recursion depth exceeded while calling a Python object


# ==== Recursion Limit ====
import sys

print("Defalt Recursion Limit:", sys.getrecursionlimit())

sys.setrecursionlimit(4000)
print("After Recursion Limit:", sys.getrecursionlimit())
