# Modify Letters using Reg Ex

def modifyString (MadString):
    import re
    MadEx = re.compile(r"(?i)(?:Lib)\_{1,3}(verb|person|people|place|thing|noun(s)*|adj([ective])*)")

    while len(MadEx.findall(MadString)) != 0:
        a = 'a'
        inputItem = MadEx.search(MadString).group(1)
        
        if  bool(re.match('adj',inputItem,re.I)):
            inputItem = 'adjective'
            a = 'an'
        if  bool(re.match('nouns',inputItem,re.I)):
            inputItem = 'plural noun'

        InPut = str(input('Enter %s %s: ' %(a,inputItem)))
        MadString = MadEx.sub(InPut,MadString,1)
        
    return MadString


def modifyList (MadList):
    OutputLetter = []
    
    for i in range(0,(len(MadList))):

        MadString = MadList[i]
        modifyString(MadString)
        OutputLetter.insert(i,MadString)

    return OutputLetter

