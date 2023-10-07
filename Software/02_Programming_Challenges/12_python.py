"""
* Write a function that receives a text and returns true or
* false (Boolean) depending on whether or not they are palindromes.
* A Palindrome is a word or expression that is the same when read
* from left to right as from right to left.
* Spaces, punctuation marks, and accents are not taken into account.
* Example: Ana lleva al oso la avellana.
"""
import dplython as dp

def is_palindrome (Sentence:str):

    Sentence = remove_non_desired(Sentence)   
    
    return Sentence == Sentence[::-1]

def remove_non_desired (Sentence:str):
    Sentence = Sentence.lower()
    Sentence = Sentence.replace(" ","")
    Sentence = Sentence.replace(".","")
    Sentence = Sentence.replace("?","")
    Sentence = Sentence.replace(";","")
    Sentence = Sentence.replace(",","")
    Sentence = Sentence.replace("¿","")

    return Sentence

str = "Ana lleva al oso la avellana"
print(is_palindrome(str))

str = "Ana"
print(is_palindrome(str))