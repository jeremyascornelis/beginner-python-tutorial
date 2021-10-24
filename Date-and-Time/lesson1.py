#Dates
import datetime

x = datetime.datetime.now() #to know the date and time now.

print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)

#If you don't want to print the time of the present
#you can just use this: datetime.datetime(year, month, day) -> to make your own time
print("\n")

mytime = datetime.datetime(2050, 11, 16)

print(mytime)
print(mytime.year)
print(mytime.month)
print(mytime.day)