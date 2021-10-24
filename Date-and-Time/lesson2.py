#strftime

import datetime

x = datetime.datetime.now()

print(x.strftime("%B")) #%B to print the month
print(x.strftime("%A")) #%A to print the day
print(x.strftime("%a")) #%a to print only 3 first word in day's name. For example: Friday -> Fri
print(x.strftime("%p"))

"""
More info, you can check this link: https://stackabuse.com/how-to-format-dates-in-python/
and also this link https://docs.python.org/3/library/datetime.html
"""