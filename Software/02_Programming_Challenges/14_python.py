"""
* Write a function that calculates whether a given number is an Armstrong number 
* (also known as a narcissistic number).
"""

import math
import re


def is_armstrong_number(num:int):
    
    num_list = list(str(num))
    length = int(math.log10(num)) + 1 
    res = 0
    for i in num_list:
        res = res + int(i)**length
    
    if res == num:
        return True
    else:
        return False

print(is_armstrong_number(157))
print(is_armstrong_number(153))
