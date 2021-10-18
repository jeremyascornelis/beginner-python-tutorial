#Functions, user inputs, and parameters

def add(x, y):
    z = x + y
    return z

number1 = int(input("Enter the first value: "))
number2 = int(input("Enter the second value: "))

print(add(number1,number2))

#number1 and number2 will become parameters for add's function.
#It will replace x with number1 and y with number2, that's parameters
#If the function is contain of 2 parameter and you only enter 1 parameter, it will cause an error