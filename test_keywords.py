from random import *
from collections import Counter
import re
import string
import time
import os




thingWord = ["$noun","noun","$VERB"]

key = set("$")

cnt = Counter()

for word in thingWord:
    cnt[word] += 1


for word in thingWord:
    if key & set(word):
        r=word.split("$")
        print(r[1])
        

   
blue = cnt.get("$")
