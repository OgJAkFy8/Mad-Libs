from random import *
from collections import Counter
import re
import string

# Open the file
txtfile = open('.\campletter1.txt','r')
Message = txtfile.read()
txtfile.close()

print(4 * '\n')

# User input version
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

actionWord.clear()
personWord.clear()
thingWord.clear()

print(blue)
print(red)
print(green)

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

print(4 * '\n')

# print the new message
print(printMes2)
