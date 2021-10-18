#Logical operators
"""
1. and
2. or
3. not
"""
#and will display true if all the statement are True
print("===and===")
print((3 > 2) and (4 > 2)) #True
print((3 > 2) and (2 > 4)) #False
print((3 < 2) and (4 > 2)) #False
print((3 < 2) and (2 > 4)) #False

print("\n")

#or will display false if all the statement are False
print("===or===")
print((3 > 2) or (4 > 2)) #True
print((3 > 2) or (2 > 4)) #True
print((3 < 2) or (4 > 2)) #True
print((3 < 2) or (2 > 4)) #False

print("\n")

print("===not===")
print(not(3 > 2)) #False