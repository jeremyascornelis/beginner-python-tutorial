#nested condition

number1 = int(input("Enter a value: "))
number2 = int(input("Enter a value: "))

if(number1 >= number2):
    if(number1 == number2):
        print("number1 is equal to number2")
    else:
        print("number1 is greater than number2")
else:
    if(number1 <= number2):
        if(number1 == number2):
            print("number1 is equal to number2")
        else:
            print("number1 is less than number2")