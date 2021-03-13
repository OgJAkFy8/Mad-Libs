# Modify mad-libs using RegEx.
# These will most often be referred to as "letters", because the original
# idea behind this program was to create letters home from summer campers.


def modifyString(MadString):
    import re

    propername = False

    MadEx = re.compile(r"(?i)(?:Lib)\_{1,3}(verb|person|people|place|thing|job|noun(s)*|adj([ective])*)")

    while len(MadEx.findall(MadString)) != 0:
        a = 'a'
        inputItem = MadEx.search(MadString).group(1)

        if bool(re.match('adj', inputItem, re.I)):
            inputItem = 'adjective'
            a = 'an'
        if bool(re.match('nouns', inputItem, re.I)):
            inputItem = 'plural noun'
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
