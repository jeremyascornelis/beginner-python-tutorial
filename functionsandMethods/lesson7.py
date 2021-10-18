#The anonymous functions
"""
These are called anonymus because they are not declared in the standard manner by using the def keyword.
You can use the lambda keyword to create small anonymous functions

> Lambda forms can take any number of arguments but return just one value in the form of an expression.
They can't contain commands or multiple expressions
> An anonymous function can't be a direct call to print because lambda requires an expression.
> Lambda functions have their own local namespace and can't access variables othe than those in their parameter list and those in the global namespace
> Although it appears that lambdas are one-line version of a function, they are not equivalent to inline statements in C or C++
"""

#Example
sum = lambda arg1, arg2: arg1 + arg2
print("Value of total: ", sum(12,15))
print("Value of total: ", sum(10,20))