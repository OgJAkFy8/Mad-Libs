from collections import Counter
import re, string, time, os


# Open the file
def file_blank():
    blankfiles = os.listdir('../Blank-Letters')
    i=1
    for b_file in blankfiles:
        #print(i+". "+b_file)
        print(str(i)+'. '+b_file)
        i=i+1
    txtfilenum =input("Enter number of the template: ")
    txtfile = open('Blank-Letters/'+blankfiles[int(txtfilenum)-1],'r')
    Message = txtfile.read()
    txtfile.close()
    print(Message)
    lst_letter = Message.split()
    #print(lst_letter)
    return lst_letter


# User input version
def file_work():
    # Assignments
    key = set("$")
    i=1
    Message = lst_letter = []
    filename = "t"
    
    blankfiles = os.listdir('Blank-Letters')
    for b_file in blankfiles:
        #print(i+". "+b_file)
        print(str(i)+'. '+b_file)
        i=i+1
    txtfilenum =input("Enter number of the template: ")

    txtfile = open('Blank-Letters/'+blankfiles[int(txtfilenum)-1],'r')
    Message = txtfile.read()
    txtfile.close()

    print(2 * '\n')

    #Convert message to working variables
    lst_letter = Message.split()

    # File Name
    filename = lst_letter[0]+"-"+lst_letter[1]
    del lst_letter[0]
    del lst_letter[0]
    ##
    str_letter = ' '.join(map(str, lst_letter))

    return str_letter, filename



def file_out(filename,msg_out):
    # Create output file and write
    # File Name
    timestr = time.strftime("%d%M%S")
    #print (filename)
    f = open('Outputs/'+filename+'_'+timestr+'.txt', 'w')
    f.write(msg_out)
    f.close()
    fin_msg = ('Outputs/'+filename+'_'+timestr+'.txt')
    return fin_msg


