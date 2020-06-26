import sys

alphabet = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

phrase = input("Fraza do zakodowania: ")
move = input("Przesunięcie: ")

encodePhrase = ""
spaces = []

for pos, char in enumerate(phrase):
    if char == " ":
        spaces.append(pos)
try: 
    int(move)
    for letter in phrase:
        if letter in alphabet or " " in phrase:
            if letter != " ":
                pos = int(alphabet.index(letter)) + int(move)
                if pos > len(alphabet)-1:
                    pos = pos - len(alphabet)
                    print(pos)
                encodePhrase += alphabet[int(pos)]
        else: 
            sys.exit("Nieprawidłowa fraza") 
except ValueError:
    sys.exit("Nieprawidłowa wartość")

word = ""

if spaces:
    encodePhrase = list(enumerate(encodePhrase))
    encodePhraseList = []
    for i, letter in encodePhrase:
        encodePhraseList.append(letter)
    i = 0
    for space in spaces:
        encodePhraseList[space - i] = " " + encodePhraseList[space - i]
        i += 1
    for letter in encodePhraseList:
        word += letter
    print(word)
else:
    print(encodePhrase)