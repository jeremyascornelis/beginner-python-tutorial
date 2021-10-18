#convertors
c = input("Enter the temperature in Celcius: ")
c = int(c)
f = (9/5)*c + 32

print(int(f))

print("\n")

m = input("Enter the number of minutes: ")
s = input("Enter the number of seconds: ")
h = int(m)/60 + int(s)/3600

print(h)