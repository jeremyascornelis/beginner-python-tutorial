#Modifying Functions
def div(a,b):
    if(b == 0):
        return "This is not possible"
    else:
        c = a/b
        return c

a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
print(div(a,b))