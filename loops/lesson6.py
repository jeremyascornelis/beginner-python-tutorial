#Continue Statement

listColor = ["red", "green", "blue", "yellow", "black", "white"]

#We will print all elements except yellow

for i in listColor:
    if i == "yellow":
        continue
    print(i)