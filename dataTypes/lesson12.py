#Dictionary

#use {} 
#use key and value
from typing import Dict


dict1 = {"number": 1, "name": "Kevin", "age": 25}

#dictionary can be manipulated
print(dict1["number"])
print(dict1["name"])
print(dict1["age"])

#change
dict1["age"] = 20

print(dict1)

print(len(dict1))

#adding element in dictionary
dict1["year"] = 2021
print(dict1)

#remove element
dict1.pop("number") #use key as the parameter
print(dict1)

#to get the item that popped
print(dict1.popitem())