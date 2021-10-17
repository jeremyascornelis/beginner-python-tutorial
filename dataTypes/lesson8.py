#Indexing and Slicing

x = "water"
#indexing starting from 0
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

#reverse version (starting from -1)
print("Reverse")

print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
print(x[-5])

print("\n")
#we have method replace to replace any character in a string
y = "Hello World"
print(y[6]) #'w'

print(y.replace('l', 'a')) #replace l with a

#slicing
a = "hello world"

print(a[1:5]) #ello
print(a[6:11]) #world
print(a[-3:-1]) #rl
print(a[:5])