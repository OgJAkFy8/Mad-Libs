from random import *
from collections import Counter
import re, string, time, os, sys
from time import sleep


# Assignments
key = set("$")
sign = "$"
i=1
k=0

# Clear the screen
print(30 *'\n')

# Open the file
blankfiles = os.listdir('blank')
for b_file in blankfiles:
    #print(i+". "+b_file)
    print(str(i)+'. '+b_file)
    i=i+1

txtfilenum =input("Enter number of the template: ")
txtfile = open('blank/'+blankfiles[int(txtfilenum)-1],'r')
Message = txtfile.read()
txtfile.close()

# Count the words in the text
k = (Message.count('$')-0)
    
# Clear the screen
print(30 *'\n')

# Convert message to working variables
lst_letter = Message.split()

# File Name
filename = lst_letter[0]+"-"+lst_letter[1]
del lst_letter[0]
del lst_letter[0]

str_letter = ' '.join(map(str, lst_letter))


# Find the words to replace.
# Have the user enter the words
# Replace the words
for word in lst_letter:
    if key & set(word):
        word_key=word.split("$")
        word_replacement=(input(str(k)+". Enter a/an "+word_key[1]+": "))
        str_letter = str_letter.replace(word, word_replacement,1)
        k=k-1

# Create output file and write
# File Name
timestr = time.strftime("%d%M%S")
#print (filename)
f = open('finished/'+filename+'_'+timestr+'.txt', 'w')
f.write(str_letter)
f.close()


# Clear the screen
print(30 *'\n')

# Print status bar
for i in range(5):
    sleep(0.5)
    print((5-i) *'\r*')
    
# print the new message
print('\n')
print(str_letter)
print('\n')
print('finished/'+filename+'_'+timestr+'.txt')
