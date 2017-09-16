from random import randint
import os, sys


def MadLib(x,y):
        #actionWord = ["hit", "climb","run"]
        #personWord = ["bar tender","baseball Ump","trash man"]
        #thingWord = ["Person","Place"]
        print("In Madlib",x)
        print(x)
        print(y)
        actionWord = []
        personWord = []
        thingWord = []

        z=1
        a=0
        while a < x:
                a += 1
                print("a-",a)
                actionWord.insert(a,input("Enter action word: "))
        a=0
        while a < y:
                a += 1
                personWord.insert(a,input("Enter a person's job (Bar Tender): "))
        a=0
        while a < z:
                a += 1
                thingWord.insert(a,input("Enter a thing word: "))

        j = len(actionWord)-1
        k = len(personWord)-1
        h = len(personWord)-1
        #printMess = 'We are having the best time in ' + personWord[randint(0,k)] +' camp.  The %s likes to %s a pinecone.'%(personWord[randint(0,k)],actionWord[randint(0,j)])
        #print(printMess)
        print(actionWord)
        return

#We are having the best time in personWord camp.  The personWord likes to actionWord a pinecone.  I find that actionWord a thingWord around makes the days go quicker.  I can't wait to see you and the thingWord soon.

def Math(eqChoice):
        x = 25
        y = 5
        z = 2

        if eqChoice == "1":
                print('x/y = ', x/y)
        elif eqChoice == "2":
                print('x//y = ', x//y)
        else:
                print("z*x = ", z*x)
        return[x,y,z]


def wordCounting ():
        import re
        from collections import Counter
        f=open('.\MadCamp.txt', 'r')
        passage = f.read()
        words = re.findall(r'\w+', passage)
        cap_words = [word.upper() for word in words]
        # Converting to uppercase so that 'Is' & 'is' like words  should be  considered as same words
        word_counts = Counter(cap_words)
        print(passage)
        print(cap_words)
        print(word_counts)
        return

def wordCountingLoop():
        actionWordNum = 0
        personWordNum = 0
        thingWordNum = 0
        file=open('.\MadCamp.txt', 'r')
        wordCount={"actionWord":0, "personWord":0,"thingWord":0}
        for word in file.read().split():
            if word in wordCount: wordCount[word] += 1
            print (word,wordCount)
        file.close();
        actionWordNum = wordCount["actionWord"]
        personWordNum = wordCount["personWord"]
        thingWordNum = wordCount["thingWord"]
        #print("action Num = ",actionWordNum)
        #print("person Num = ",personWordNum)
        print(actionWordNum,personWordNum)
        return(actionWordNum,personWordNum,thingWordNum)


def wordCounterfrmt():
        file=open('.\MadCamp.txt', 'r', encoding="utf-8-sig")
        from collections import Counter
        wordcount = Counter(file.read().split())
        for item in wordcount.items(): print("{}\t{}".format(*item))
        file.close();
        return

def replaceWords():
        f1 = open('.\MadCamp.txt', 'r')
        f2 = open('.\MadCamp-tmp.txt', 'w')
        i=-1
        rtext = ""
        
        strText = f1.read().split()
        strText
        print(strText[3])
        for  aWord in strText:
                if aWord == "actionWord":
                        rtext = input("Enter action word: ")
                        f2.write(aWord.replace('actionWord',(' '+rtext)))
                elif aWord == "personWord":
                        rtext = input("Enter person word: ")
                        f2.write(aWord.replace('personWord',(' '+rtext)))
                else:
                        f2.write((' '+aWord))
                        print((' '+aWord))
        #output.write(s.replace(stext, rtext))
        #strText.replace('personWord', 'personWord%s' %i)
        #strText.replace('thingWord', 'thingWord%s' %i)
           #print(strText)
        #f2.write(strText)
        f1.close()
        f2.close()
        return

actionWordNum = 9
personWordNum = 0
#MadLib()
#wordCounterfrmt()

print("\n\n================================================================")

#MadLib()
#print("\n==========================")

#actionWordNum, personWordNum = wordCountingLoop()
wordCountingLoop()
print("main",actionWordNum, personWordNum)
print("\n^^^^^^^^^^^^^^^^^^^^^^^^^")
MadLib(actionWordNum, personWordNum)
#replaceWords()

