import modules.fileModule as fm

file_path,filename = fm.Select_Letter('c:\\Users\\erika\\Documents\\GitHub\\Mad-Libs\\Blank-Letters')
print(' Need Mad Lib program here') # Need Mad Lib program here
Letter, filename = fm.Assemble_Letter(file_path,filename)
fm.Write_Letter('C:\\Users\\erika\Documents\\GitHub\\Mad-Libs\\Outputs',filename,Letter)
