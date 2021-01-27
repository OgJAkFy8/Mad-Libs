## Welcome to Mad-Libs in Python

When I started this years ago, I had ideas of the folder structure that does not seem to be figured out by me at this time.

## How to use it
1. Open or run the start_MadLibs.py file. 
1. Answer the questions. 
1. Read the output file. 

## Root Folder
**./Mad-Libs** - 

## Root Folder Structure
- **./Blank-Letters** - The program started from the idea of someone writing home from summer camp.  The "Letters" are the templates that need will be modified by the program when run. 
- **./Examples** - A place for the earlier programs that still work. 
- **./Incomplete** - This is where the older programs went to die. 
- **./modules** - The current program was built using modules.  This mostly due to the way I was building it.  I started using other parts of the older programs and put them into functions (def) which are called through the main program 'start_MadLibs.py' .  
- **./Outputs** - This folder holds the completed "Letters".  It is also in the .gitignore file, so that it is not replicated. 

## Root Files
- **./.gitignore** - Prevents the Output files from being replicated. 
- **./README.md** - This file. 
- **./start_MadLibs.py** - The main "Mad-Libs" program. 

## Program Files
- **./start_MadLibs.py** - Starts the program.  
  - Calls the following modules: 
    - import modules.fileModule as fm 
    - import modules.madregexModule as ml 
    - import tkinter as tk 
    - from tkinter import messagebox 
	
- **./modules/fileModule.py** - 
- **./modules/madregexModule.py** - 
- **./Blank-Letters/ShortLetter.txt
- **./Blank-Letters/campletter.txt
- **./Outputs/Letter-Home_235036.txt**




Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/OgJAkFy8/Mad-Libs/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
