file = open("testList.txt", "r")

x = file.read()

print(x)

"""
Sometimes you can get error that say that the coding error or encoding error.
This is the solution:
file = open("testList.txt", "r", encoding = "utf-8")
"""