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
print(blankfiles)
i=1
for b_file in blankfiles:
    #print(i+". "+b_file)
    print(str(i)+'. '+b_file)
    i=i+1
txtfilenum =input("Enter number of the template: ")

txtfile = open('blank/'+blankfiles[int(txtfilenum)-1],'r')
Message = txtfile.read()
t = Counter(Message)
txtfile.close()
h=t["$"]
print(t["$"])
print("DEBUG -----T $ -----------<<<<<<")
print(1 * '\n')

# User input version
printMess = Message.split()
printMes2 = Message

# File Name
filename = printMess[0]+"-"+printMess[1]
print(filename)
print("DEBUG -------FILENAME ---------<<<<<<")
print(1 * '\n')

# Clean up file
printMess.remove(printMess[0])
printMess.remove(printMess[0])


key = set("$")
cnt = Counter()


# Count the words in the text
for word in printMess:
    cnt[word] += 1

green = cnt.get("$")
print(green)
print("DEBUG ---GREEN -------------<<<<<<")
print(1 * '\n')



# Select the key words
blue = cnt.get('thingWord')
red = cnt.get('personWord')
green = cnt.get('$')

new_list = [x for x in actionWord if re.search('$', x)]
for item in new_list:
    print(item)


actionWord.clear()
personWord.clear()
thingWord.clear()

# print(blue)
# print(red)
# print(green)
j=1
for word in printMess:
    if key & set(word):
        r=word.split("$")
        print(actionWord[j])
        actionWord.insert(j,input("Enter "+r[1]+": "))
        o = actionWord[j]
        j +=1
        printMes2 = printMes2.replace(word, o,1)

        print("DEBUG j ----------->>>>> "+j)
        print(1 * '\n')

        # Enter the words
##        for i in range(0,h):
##            actionWord.insert(i,input("Enter "+r[1]+": "))
##            o = actionWord[i]
##            printMes2 = printMes2.replace(word, o,1)
print("DEBUG ----GREEN ------------>>>>> "+green)
print(1 * '\n')



# Enter the words
# if green != None:
#     for i in range(0,green):
#         actionWord.insert(i,input("Enter action word: "))
#         o = actionWord[i]
#         printMes2 = printMes2.replace('actionWord', o,1)

# if blue != None:
#     for i in range(0,blue):
#         thingWord.insert(i,input("Enter thing word: "))
#         o = thingWord[i]
#         printMes2 = printMes2.replace('thingWord', o,1)

# if red  != None:
#     for i in range(0,red):
#         personWord.insert(i,input("Enter person's job title: "))
#         o = personWord[i]
#         printMes2 = printMes2.replace('personWord', o,1)

#print(4 * '\n')

# Create output file and write
# File Name
timestr = time.strftime("%d%M%S")
#print (filename)
f = open('finished/'+filename+'_'+timestr+'.txt', 'w')
f.write(printMes2)
f.close()

# print the new message
print(printMes2)
print('finished/'+filename+'_'+timestr+'.txt')
