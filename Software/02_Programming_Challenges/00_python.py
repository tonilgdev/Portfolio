"""
  Write a program that displays by console (with a print) 
  numbers from 1 to 100 (both included and with a line break between each printout), replacing the following
  each print), substituting the following:
  - Multiples of 3 for the word "fizz".
  - Multiples of 5 for the word "buzz".
  - Multiples of 3 and 5 at the same time for the word "fizzbuzz".
"""

i = 0
while i <= 100:
    i +=1 
    if i%3 == 0:
        if i%5 == 0:
            print("fizzbuzz\n")
        else:
            print("fizz\n")
    elif i%5 == 0:
        print("buzz\n")
    else:
        print(f"{i}\n")
