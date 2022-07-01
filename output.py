

class Output(object):


    def __init__(self):
        self._toBeDisplayed={}

        self._toBeDisplayed['team']=[]
        self._toBeDisplayed['content']=[]
        self._toBeDisplayed['map']=[]

    @property
    def toBeDisplayed(self):
        return self.transformOutput()

    def team(self, txt):
        self._toBeDisplayed['team'].append(txt)

    def content(self, txt):
        self._toBeDisplayed['content'].append(txt)

    def map(self, txt):
        self._toBeDisplayed['map'].append(txt)

    def reset(self):
        for key in self._toBeDisplayed:
            self._toBeDisplayed[key]=[]
''' 
    def transformOutput(self):
        outputAsArray={}
        for key in self._toBeDisplayed:
            outputAsArray[key]=Output.splitText(self._toBeDisplayed[key])
        return outputAsArray
instead of that we automatically split with array of Message
    @staticmethod
    def splitText(txt):
        if txt!="" and txt!=None:
            return txt.split('\n')
        elif type(txt)==str:
            return txt
        else:
            return ""
'''