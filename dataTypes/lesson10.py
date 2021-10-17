#List
listColor = ["red", "green", "yellow", "blue", "black", "white"]
randomList = ["red", "green", "yellow", "blue", "black", "white", 3, 5.45]

print(listColor)

#If you want to know methods of list, you can type: dir(list) in your cmd 

#access the element in a list
print(listColor[0]) #red
print(listColor[2]) #yellow
print(listColor[-1]) #white

#len is to know how much elements in a list
print(len(listColor))

#print the last element in a list and remove that
print(listColor.pop())
print(listColor) #['red', 'green', 'yellow', 'blue', 'black']

#add element as the last element in a list
listColor.append("purple")
print(listColor) #['red', 'green', 'yellow', 'blue', 'black', 'purple']