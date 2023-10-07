"""
 * Write a program to check whether a number is prime or not.
 * When this is done, print out the prime numbers between 1 and 100.
"""
def prime_number (num: int):

    if (num <= 1):
        return False
    elif (num%2 == 0 and num > 2):
        return False
    else:
        i = 2
        while i < round(num**0.5):
            if (num%i == 0 and num == i):
                return False
            i+=1
        return True

i = 1
while i < 100:
    if(prime_number(i)):
        print(f"{i} ")
    i+=1