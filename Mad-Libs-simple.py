from random import *
from collections import Counter
import re
import string

# Simple Replace
actionWord = ["hit", "climb","run"]
personWord = ["bar tender","baseball Ump","trash man"]
thingWord = ["boat"]

printMess = 'We are having the best time in %s camp.  The %s likes to %s a pinecone.'%(personWord[randint(0,len(personWord))],personWord[randint(0,len(personWord))],actionWord[randint(0,len(actionWord))])
print(printMess)
print(4 * '\n')
