"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

MAX_WORD_LENGTH = random.randint(4,11)
FORMAT = "cv"
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = ''
for i in range (0, MAX_WORD_LENGTH):
    word_format += random.choice(FORMAT)
print(word_format)

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)

