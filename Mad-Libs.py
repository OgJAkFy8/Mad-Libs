from random import *
from collections import Counter
import re
import string


# Simple Replace
actionWord = ["hit", "climb","run"]
personWord = ["bar tender","baseball Ump","trash man"]
nounWord = ["boat"]

printMess = 'We are having the best time in %s camp.  The %s likes to %s a pinecone.'%(personWord[randint(0,len(personWord))],personWord[randint(0,len(personWord))],actionWord[randint(0,len(actionWord))])
print(printMess)
print(4 * '\n')




# User input version
# Start with the same text
Message = 'We are having the best time in nounWord camp.  The personWord likes to actionWord a pinecone.'
printMess = Message.split()
printMes2 = Message

# Count the words in the text 
cnt = Counter()
for word in printMess:
    cnt[word] += 1

# Select the key words
blue = cnt.get('nounWord')
red = cnt.get('personWord')
green = cnt.get('actionWord')

actionWord.clear()
personWord.clear()
nounWord.clear()

# Enter the words
for i in range(0,green):
	actionWord.insert(i,input("Enter action word: "))
	o = actionWord[i]
	printMes2 = printMes2.replace('actionWord', o,1)

for i in range(0,blue):
	nounWord.insert(i,input("Enter noun word: "))
	o = nounWord[i]
	printMes2 = printMes2.replace('nounWord', o,1)

for i in range(0,red):
	personWord.insert(i,input("Enter person's job title: "))
	o = personWord[i]
	printMes2 = printMes2.replace('personWord', o,1)
	
print(4 * '\n')

# print the new message
print(printMes2)
