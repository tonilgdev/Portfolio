"""
* Write a function that calculates and returns the factorial of a given number recursively.
"""

def factorial (num:int):

    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(3))

print(factorial(5))

print(factorial(10))