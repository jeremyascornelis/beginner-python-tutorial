#String formatting
#is just an arranging things in order

x = "is"
y = "my"
z = "name"

c = y + " " + z + " " + x
print(c)
#arrange those words to become an sentence that have meaning 

a = " my name is "
b = "Jimmy"
d = "my name is {}".format(b)
print(d)

#another way
e = "my name is " + b
print(e)

#another example
name = "Alex"
age = 20
sentence = "My name is {} and my age is {}".format(name, age)

print("\n")
print(sentence)

#another way
sentence1 = f"My name is {name} and my age is {age}"
print(sentence1)

#another example
list1 = ["Freddy", "sports", 25]
#This will be work by the index
sentence2 = f"My name is {list1[0]} and my hobby is playing {list1[1]} and my age is {list1[2]}"
print(sentence2)
