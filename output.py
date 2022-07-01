from message import Message

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
        if isinstance(txt,Message):
            self._toBeDisplayed['team'].append(txt)
        elif isinstance(txt, list):
            for elem in txt:
                self._toBeDisplayed['team'].append(elem)

        

    def content(self, txt):
        if isinstance(txt,Message):
            self._toBeDisplayed['content'].append(txt)
        elif isinstance(txt, list):
            for elem in txt:
                self._toBeDisplayed['content'].append(elem)
        

    def map(self, txt):
        if isinstance(txt,Message):
            self._toBeDisplayed['map'].append(txt)
        elif isinstance(txt, list):
            for elem in txt:
                self._toBeDisplayed['map'].append(elem)
        

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