#Identity Operators
"""
1. is
2. is not
"""
print("===Identity Operators===")

number1 = 3
number2 = 3
number3 = 7

print(number1 is number2) #True
print(number2 is number3) #False
print(number1 is not number3) #True
print(number1 is not number2) #False

#Membership Operators
"""
1. in
2. not in
"""
print("\n===Membership Operators===")

listNumber = [1,2,3,4,5]

print(4 in listNumber) #True
print(10 in listNumber) #False
print(10 not in listNumber) #True
print(4 not in listNumber) #False

print("\n")

sentence1 = "water is life"

print("e" in sentence1) #True
print("z" in sentence1) #False