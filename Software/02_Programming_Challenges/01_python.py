"""
* Write a function that receives two words (String) and returns 
* true or false (Bool) depending on whether or not they are anagrams.
* - An Anagram consists of forming a word by rearranging 
*   ALL the letters of another initial word.
* - It is NOT necessary to check that both words exist.
* - Two exactly identical words are not anagrams. 
"""

first_word = input("Please enter a word: ")
second_word = input("Please enter a second word: ")

if(first_word == second_word):
    print("False")
    exit()

for i in second_word:
    if first_word.rfind(i) != -1: #
        if (i == second_word[-1]):
            print(True)
    else:
        print("False")
        exit()
