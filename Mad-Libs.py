from random import randint
actionWord = ["hit", "climb","run"]
personWord = ["bar tender","baseball Ump","trash man"]
a=3
while a < 6:
	a += 1
	actionWord.insert(a,input("Enter action word: "))

j = len(actionWord)-1
printMess = 'We are having the best time in %s camp.  The %s likes to %s a pinecone.'%(personWord[randint(0,2)],personWord[randint(0,3)],actionWord[randint(0,j)])
print(printMess)


