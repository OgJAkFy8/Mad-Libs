import re

TrumpAns = []
# For testing
MadLib = 'The liB_AdjecTive Lib_verb and a Lib__adj to the now in the Lib_noun.'
####

MadLib = TrumpLib = [
"You have to Lib_verb anyway, so why not Lib_verb big?",
"I'm a bit of a P. T. Barnum. I make Lib_nouns out of everyone.",
"The point is that you can't be too Lib_verb.",
"Sometimes by losing a Lib_noun you find a new way to win the Lib_noun.",
]

TrumpOrg = (
"You have to think anyway, so why not think big?",
"I'm a bit of a P. T. Barnum. I make stars out of everyone.",
"The point is that you can't be too greedy.",
"Sometimes by losing a battle you find a new way to win the war.",
)

MadEx = re.compile(r"(?i)(?:Lib)\_{1,3}(verb|noun(s)*|adj([ective])*)")

for i in range(0,(len(MadLib))):

    MadString = MadLib[i]
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
    TrumpAns.insert(i,MadString)

 
# For testing
for i in range(0, len(TrumpAns)):
    #print(TrumpOrg[i])
    print(TrumpAns[i])
####


