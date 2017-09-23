from random import *
from collections import Counter
import re
import string

# 
# -------------------- The user editable section --------------------------------
# Enter the list of words that will be randomly selected.
actionWord = ["hit", "climb","run"]
personWord = ["bar tender","baseball Ump","trash man"]
thingWord = ["boat"]

# Start with the message
# Write the message below.  Use the thingWord, personWord and actionWord for the "blanks"
Message = 'We are having the best time in thingWord camp.  The personWord likes to actionWord a pinecone.'
#
# --------------------------------------------------------------------------



# The program
# Print four blank lines to create a gap in the output
print(4 * '\n')

# Change the string to a list
printMess = Message.split()
printMes2 = Message

# Count the words in the text
cnt = Counter()
for word in printMess:
    cnt[word] += 1

# Select the key words
blue = cnt.get('thingWord')
red = cnt.get('personWord')
green = cnt.get('actionWord')

# Enter the words
for i in range(0,green):
    o = actionWord[randint(0, (len(actionWord)-1))]
    printMes2 = printMes2.replace('actionWord', o,1)

for i in range(0,blue):
    o = thingWord[randint(0, (len(thingWord)-1))]
    printMes2 = printMes2.replace('thingWord', o,1)

for i in range(0,red):
    o = personWord[randint(0, (len(personWord)-1))]
    printMes2 = printMes2.replace('personWord', o,1)

#print(4 * '\n')

# print the new message
print(printMes2)
