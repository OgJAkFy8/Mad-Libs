import modules.fileModule as fm
import modules.madregexModule as ml
import tkinter as tk
from tkinter import messagebox


def popup(message, title=None):
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    messagebox.showinfo(title, message, parent=root)
    root.destroy()

file_path,filename = fm.Select_Letter('c:\\Users\\erika\\Documents\\GitHub\\Mad-Libs\\Blank-Letters')
BlankLetter, filename = fm.Assemble_Letter(file_path,filename)
Letter = ml.modifyString(BlankLetter)
MsgPath, Message = fm.Write_Letter('C:\\Users\\erika\Documents\\GitHub\\Mad-Libs\\Outputs',filename,Letter)

popup(Message, MsgPath)
