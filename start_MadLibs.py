#from modules.fileModule import Assemble_Letter, Select_Letter, Write_Letter
#from modules.madregexModule import modifyString
import tkinter as tk
from tkinter import messagebox
import os
import time


# BEGIN
# Variables
stationaryPad = 'Blank-Letters'
mailBox = 'Outputs'

# Pop-up window for viewing the output
def popup(message, title=None):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    messagebox.showinfo(title, message, parent=root)
    root.destroy()


def validate_path(chk_path):
    d_path = chk_path
    try:
        chk_path = chk_path.replace('\\', '/')
    except:
        chk_path
    if os.path.isdir(chk_path):
        if not chk_path.endswith('/'):
            d_path = chk_path + '/'
    if os.path.isfile(chk_path):
        d_path = os.path.dirname(chk_path) + '/'

    return d_path

# File Module
# Select the file.  Function returns the full path of the file.
def Select_Letter(dir_path):
    numSelection = 0
    dir_path = validate_path(dir_path)
    file_list = os.listdir(dir_path)
    for i in range(len(file_list)):
        print(str(i) + '. ' + file_list[i - 1])

    numSelection = eval(input("Enter number to select: "))
    filename = file_list[int(numSelection) - 1]
    file_path = dir_path + filename
    return file_path, filename


# User input version
def Assemble_Letter(file_path, filename='None'):
    # Assignments
    key = set("$")
    i = 1
    Message = letterAslist = []

    try:  # trying the "try except" statement
        file_path = file_path.replace('\\', '/')
    except:
        file_path

    if filename == 'None':
        splitpath = file_path.split('/')
        filename = splitpath[len(splitpath) - 1]

    txtfile = open(file_path, 'r')
    Message = txtfile.read()
    txtfile.close()

    # print(2 * '\n')

    # Convert message to working variables
    letterTitle = (Message.split('\n', 1)[0]).split(':')[1]
    MessageAslist = Message.split('\n', 1)[1]
    letterAslist = MessageAslist.split()

    print(letterTitle)

    # File Name
    filename = letterTitle.replace(' ', '-')
    ##
    str_letter = ' '.join(map(str, letterAslist))

    return str_letter, filename


def Write_Letter(dir_path, filename, message):
    # Create output file and write
    f_ext = 'txt'  # Default extension if there isn't one passed.
    timestr = time.strftime("%d%M%S")  # Time stamp for filename
    d_path = validate_path(dir_path)  # Directory Path

    # Build Filename
    if '.' in filename:
        f_name, f_ext = os.path.splitext(filename)
    else:
        f_name = filename

    file_path = '%s%s_%s.%s' % (d_path, f_name, timestr, f_ext)

    # Open, write, and close the letter
    f = open(file_path, 'w')
    f.write(message)
    f.close()
    fin_msg = file_path
    return fin_msg, message

# Regex Module
# Modify mad-libs using RegEx.
# These will most often be referred to as "letters", because the original
# idea behind this program was to create letters home from summer campers.


def modifyString(MadString):
    import re

    propername = False

    MadEx = re.compile(r"(?i)(?:Lib)\_{1,3}(verb(past)*|verb(ing)*|body|plant|game|person|people|place|thing|job|date|number|animal(s)*|noun(s)*|adj([ective])*)")

    while len(MadEx.findall(MadString)) != 0:
        a = 'a'
        inputItem = MadEx.search(MadString).group(1)

        if bool(re.match('adj', inputItem, re.I)):
            inputItem = 'adjective'
            a = 'an'
        if bool(re.match('nouns', inputItem, re.I)):
            inputItem = 'plural noun'
        if bool(re.match('game', inputItem, re.I)):
            inputItem = 'game'
        if bool(re.match('body', inputItem, re.I)):
            inputItem = 'part of the body'
        if bool(re.match('plant', inputItem, re.I)):
            inputItem = 'plant'
        if bool(re.match('animals', inputItem, re.I)):
            inputItem = 'plural animal'
        if bool(re.match('verbpast', inputItem, re.I)):
            inputItem = 'past tense verb'
        if bool(re.match('verbing', inputItem, re.I)):
            inputItem = 'verb ending in "ing"'
        if bool(re.match('person', inputItem, re.I)):
            inputItem = '''person's name'''
            propername = True

        InPut = str(input('Enter %s %s: ' % (a, inputItem)))
        if(propername == True):
            InPut = InPut.capitalize()
            propername = False
        MadString = MadEx.sub(InPut, MadString, 1)

    return MadString


def modifyList(MadList):
    OutputLetter = []

    for i in range(0, (len(MadList))):
        MadString = MadList[i]
        modifyString(MadString)
        OutputLetter.insert(i, MadString)

    return OutputLetter





# PROCESS
file_path, filename = Select_Letter(stationaryPad)

#print(filename)
#print(file_path)
if(file_path != 'Blank-Letters/Keywords'):
    BlankLetter, filename = Assemble_Letter(file_path, filename)
    Letter = modifyString(BlankLetter)
    MsgPath, Message = Write_Letter(mailBox, filename, Letter)
    # END
    popup(Message, MsgPath)
else:
    #print('else')
    f = open(file_path, 'r')
    t = f.read().split('\n')
    for i in range(0, (len(t))):
        print(t[i])

