"""
* Create a program that is capable of transforming natural text into Morse code and vice versa.
* - It should automatically detect what type it is and perform the conversion.
* - In Morse, dash “—”, dot “.”, a space " " between letters or symbols, and two spaces between words " " are supported.
* - The Morse alphabet supported will be the one shown in https://es.wikipedia.org/wiki/C%C3%B3digo_morse.
"""

morse_code = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "CH": "---- ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "Ñ": "--.-- ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-.. ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    ".": ".-.-.- ",
    ",": "--..-- ",
    "?": "..--.. ",
    "\"": ".-..-. ",
    "/": "-..-. ",
    " ": "  "
}

original_sentence = input("Can you write me something? ")
sentence_morse_code = str()

for i in original_sentence:
    sentence_morse_code += morse_code.get(i.capitalize())

print("Your sentence in morse code is:\n" + sentence_morse_code)