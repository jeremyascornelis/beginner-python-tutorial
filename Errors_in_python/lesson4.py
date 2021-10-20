#Type Error

"""
Error is in the type.

print(3 + "d")

TypeError: unsupported operand type(s) for +: 'int' and 'str'

This error occurs cause we want to try some operations on 2 operand that have the different data types

Another example:

a = input("enter: ")
b = input("enter: ")
c = (a + b) * 2

print(c)

//Terminal:

enter: 2
enter: 3
2323

The result is not 10 but 2323

Another example:

x = 3
a + x

Type Error: can only concatenate str (not "int") to str

Also type error will occur when you try to operate two different datatypes (except using adding operator)
For example, if you use divided operator:

"dedj" / 0

TypeError: unsupported operand type(s) for /: 'str' and 'int'

"""