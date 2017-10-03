from collections import Counter
import re, string, time, os


# Open the file
def file_blank:
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
    return Message


# User input version
def file_name(Message):
    printMess = Message.split()
    # File Name
    filename = printMess[0]+"-"+printMess[1]
    printMess.remove(printMess[0])
    printMess.remove(printMess[0])
    return filename



def file_out(filename,msg_out):
    # Create output file and write
    # File Name
    timestr = time.strftime("%d%M%S")
    #print (filename)
    f = open('finished/'+filename+'_'+timestr+'.txt', 'w')
    f.write(msg_out)
    f.close()
    fin_msg = ('finished/'+filename+'_'+timestr+'.txt')
    return fin_msg


