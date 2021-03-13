from modules.fileModule import Assemble_Letter, Select_Letter, Write_Letter
from modules.madregexModule import modifyString
import tkinter as tk
from tkinter import messagebox


# BEGIN
# Variables
stationaryPad = 'c:\\Users\\erika\\Documents\\GitHub\\Mad-Libs\\Blank-Letters'
mailBox = 'C:\\Users\\erika\\Documents\\GitHub\\Mad-Libs\\Outputs'


# Pop-up window for viewing the output
def popup(message, title=None):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    messagebox.showinfo(title, message, parent=root)
    root.destroy()


# PROCESS
file_path, filename = Select_Letter(stationaryPad)
BlankLetter, filename = Assemble_Letter(file_path, filename)
Letter = modifyString(BlankLetter)
MsgPath, Message = Write_Letter(mailBox, filename, Letter)

# END
popup(Message, MsgPath)
