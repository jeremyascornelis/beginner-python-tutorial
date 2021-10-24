#Opening and reading the file
"""
file = open("yourpathfile/yourfilename", "the method you choose")

"r" -> read
"w" -> write
"a" -> append
"""

file = open("test.txt", "r")
x = file.read()

print(x)