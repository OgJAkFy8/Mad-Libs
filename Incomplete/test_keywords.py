from random import *
from collections import Counter
import re
import string
import time
import os


str_letter = 'This is a $VERB of the $noun system'
lst_letter = str_letter.split()
del lst_letter[0]
del lst_letter[0]


str_letter = ' '.join(map(str, lst_letter))

key = set("$")


for word in lst_letter:
    if key & set(word):
        word_key=word.split("$")
        word_replacement=(input("Enter a/an "+word_key[1]+": "))
        str_letter = str_letter.replace(word, word_replacement,1)

print(str_letter)

