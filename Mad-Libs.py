from random import *
from collections import Counter
import re
import string
import time
import os


# Define the lists
actionWord = [""]
personWord = [""]
thingWord = [""]


# Open the file
blankfiles = os.listdir('blank')
i=1
for b_file in blankfiles:
    #print(i+". "+b_file)
    print(str(i)+'. '+b_file)
    i=i+1
txtfilenum =input("Enter number of the template: ")

txtfile = open('blank/'+blankfiles[int(txtfilenum)],'r')
Message = txtfile.read()
txtfile.close()

print(4 * '\n')

# User input version
printMess = Message.split()
printMes2 = Message

# File Name
filename = printMess[0]+"-"+printMess[1]
printMess.remove(printMess[0])
printMess.remove(printMess[0])

# Count the words in the text
cnt = Counter()
for word in printMess:
    cnt[word] += 1

# Select the key words
blue = cnt.get('thingWord')
red = cnt.get('personWord')
green = cnt.get('actionWord')

actionWord.clear()
personWord.clear()
thingWord.clear()

# print(blue)
# print(red)
# print(green)

# Enter the words
if green != None:
    for i in range(0,green):
        actionWord.insert(i,input("Enter action word: "))
        o = actionWord[i]
        printMes2 = printMes2.replace('actionWord', o,1)

if blue != None:
    for i in range(0,blue):
        thingWord.insert(i,input("Enter thing word: "))
        o = thingWord[i]
        printMes2 = printMes2.replace('thingWord', o,1)

if red  != None:
    for i in range(0,red):
        personWord.insert(i,input("Enter person's job title: "))
        o = personWord[i]
        printMes2 = printMes2.replace('personWord', o,1)

#print(4 * '\n')

# Create output file and write
# File Name
timestr = time.strftime("%d%M%S")
#print (filename)
f = open('finishedLetters/'+filename+'_'+timestr+'.txt', 'w')
f.write(printMes2)
f.close()

# print the new message
print(printMes2)
print('finished/'+filename+'_'+timestr+'.txt')
