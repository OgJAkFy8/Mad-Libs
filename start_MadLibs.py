from modules.fileModule import Assemble_Letter, Select_Letter, Write_Letter
from modules.madregexModule import modifyString
import tkinter as tk
from tkinter import messagebox


#def main():
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


#if __main__ == "__main__":
 #   main()