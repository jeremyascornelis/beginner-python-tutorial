#writing file

file1 = open("testList.txt", "w")
colorList = ["red", "yellow", "green", "blue", "black"]

for item in colorList:
    test = file1.write(item + "\n")