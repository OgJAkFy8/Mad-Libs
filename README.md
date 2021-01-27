## Welcome to Mad-Libs in Python
This was a project that I started with my nephews a number of years ago to teach them how to program in Python, because they were all using Minecraft.  I also wanted to relearn Python (Orignially learned with version 2.3 or something.), specifically version 3.x.  This current version has been written using Python 3.9 on a windows 10 machine.
When I started this years ago, I had ideas of the folder structure that does not seem to make sense to me at this time.  So that is going to have to be cleaned up.  

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
- **./modules/fileModule.py**
  - The file module contains: 
    - Select_Letter 
    - Assemble_Letter 
    - Write_Letter 

- **./modules/madregexModule.py** 
  - The Mad RegEx Module contains:
    - modifyList - This was used during testing so that I could pull in a bunch of strings.  The function was later split with the "String" one which is what is passed to it by the "Assemble_Letter" script.
    - modifyString - This is where the "Magic" happens.  It simply uses a RegEx (Regular Expression) to look for the _key words_ in the Blank-Letter files.
    ```
    import re
    MadEx = re.compile(r"(?i)(?:Lib)\_{1,3}(verb|person|people|place|thing|noun(s)*|adj([ective])*)") 
    inputItem = MadEx.search(MadString).group(1)
    MadEx.sub(InPut,MadString,1)
    ```
    - Above are the lines of code that does the work. As of this writing, it looks for verb, person, people place, thing, noun and adjective
    
### Input and Output
The input is build by you the programmer, the output is build by the user.

#### Input
The input files are just txt files that have been modified to have some words replaced by the keywords.
- **./Blank-Letters/ShortLetter.txt - primarily used for testing, because it only calls a couple _blanks_.
- **./Blank-Letters/campletter.txt - The _full version_ of letter template.

**_Keywords_** - Keywords are the words that are seached for during program execution.   
``` 
Lib_verb        # Action word: Jump, bet
Lib_person      # Single person: Cook, umpire
Lib_people      # Multiple people: Foosball Team, passengers
Lib_place       # Place: bus stop, LA
Lib_thing       # Thing: moon
Lib_noun(s)     # A person, place or thing - This may make way for the above
Lib_adj(ective) # A word that discribs a noun: _blue_ car

``` 

#### Building the Template files
1. On the first line of the document, type the title of the paragraph/letter.  _See **FUTURE FEATURES** below._
**EXAMPLE** _Summer Camp Diary_
1. Find a sentence or paragraph that you like. 
1. Starting on the second line paste it into a txt file. 
1. Replace the different words with the above _keywords_. 
**EXAMPLE** _The fast brown dog._ would become:
  - The fast Lib_adj Lib_thing.
  - The Lib_adverb brown Lib_noun.

#### Output
- **./Outputs/Letter-Home_235036.txt** - An example of what one of the outlook files will be named.  





Future Features
1. The user will be able to see the _TYPE_ of document they are working on.  To help tailor their responses. In otherwords, when you run the program you will have a base idea of what you are working on. 
1. Currently the user selects the _Letter_ they want to work on.  This will be made random.



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
