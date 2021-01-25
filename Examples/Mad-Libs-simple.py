from random import *
from collections import Counter
import re
import string

# Simple Replace
actionWord = ["hit", "climb","run"]
personWord = ["bar tender","baseball Ump","trash man","IT guy"]
thingWord = ["boat"]

printMess = 'We are having the best time in %s camp.  The %s likes to %s a pinecone.'%(personWord[randint(0,len(personWord)-1)],personWord[randint(0,len(personWord)-1)],actionWord[randint(0,len(actionWord)-1)])
print(printMess)
print(4 * '\n')
