

class Output(object):


    def __init__(self):
        self._toBeDisplayed={}

        self._toBeDisplayed['team']=""
        self._toBeDisplayed['content']=""
        self._toBeDisplayed['map']=""

    @property
    def toBeDisplayed(self):
        return self.transformOutput()

    def team(self, txt):
        self._toBeDisplayed['team']=self._toBeDisplayed['team']+txt

    def content(self, txt):
        self._toBeDisplayed['content']=self._toBeDisplayed['content']+txt

    def map(self, txt):
        self._toBeDisplayed['map']=self._toBeDisplayed['map']+txt

    def reset(self):
        for key in self._toBeDisplayed:
            self._toBeDisplayed[key]=""

    def transformOutput(self):
        outputAsArray={}
        for key in self._toBeDisplayed:
            self._outputAsArray[key]=Output.splitText(self._toBeDisplayed[key])
        return outputAsArray

    @staticmethod
    def splitText(txt):
        if txt!="" and txt!=None:
            return txt.split('\n')
        elif type(txt)==str:
            return txt
        else:
            return ""