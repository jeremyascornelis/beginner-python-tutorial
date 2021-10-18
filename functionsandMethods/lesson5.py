#Convertors using function

def temp(c):
    f = (9/5) * c + 32
    return f

c = int(input("Enter the temperature in celcius: "))
print(temp(c))

print("\n")

def leng(m, s):
    h = m / 60 + s / 3600
    return h

m = int(input("Enter the numbers of minutes: "))
s = int(input("Enter the numbers of seconds: "))
print(leng(m,s))