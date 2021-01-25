import os, time


def validate_path(chk_path):
    d_path = chk_path
    try:
        chk_path = chk_path.replace('\\','/')
    except:
        chk_path
    if(os.path.isdir(chk_path)):
        if(not chk_path.endswith('/')):
            d_path = chk_path+'/'
    if(os.path.isfile(chk_path)):
        d_path = os.path.dirname(chk_path)+'/'
        
    return d_path


# Select the file.  Function returns the full path of the file.
def Select_Letter(dir_path):
    numSelection  = 0
    dir_path = validate_path(dir_path)
    file_list = os.listdir(dir_path)
    for i in range(len(file_list)):
        print(str(i)+'. '+file_list[i-1])

    numSelection = eval(input("Enter number to select: "))
    filename = file_list[int(numSelection)-1]
    file_path = dir_path+filename
    return file_path,filename

# User input version
def Assemble_Letter(file_path,filename = 'None'):
    # Assignments
    key = set("$")
    i=1
    Message = lst_letter = []

    try:
       file_path = file_path.replace('\\','/')
    except:
        file_path

    if(filename == 'None'):
        splitpath = file_path.split('/')
        filename = splitpath[len(splitpath)-1]

    txtfile = open(file_path,'r')
    Message = txtfile.read()
    txtfile.close()

    #print(2 * '\n')

    #Convert message to working variables
    Split_Message = Message.split()
    lst_letter = Message.split()

    print(lst_letter[0])
    # File Name
    filename = lst_letter[0]+"-"+lst_letter[1]
    del lst_letter[0]
    del lst_letter[0]
    ##
    str_letter = ' '.join(map(str, lst_letter))

    return str_letter, filename



def Write_Letter(dir_path,filename,message):
    # Create output file and write
    f_ext = 'txt' # Default extension if there isn't one passed.
    timestr = time.strftime("%d%M%S") # Time stamp for filename
    d_path = validate_path(dir_path) # Directory Path

    # Build Filename
    if('.' in filename):
        f_name,f_ext = os.path.splitext(filename)
    else:
        f_name = filename

    file_path = '%s%s_%s.%s' %(d_path,f_name,timestr,f_ext)
    
    # Open, write, and close the letter
    f = open(file_path, 'w')
    f.write(message)
    f.close()
    fin_msg = (file_path)
    return fin_msg

