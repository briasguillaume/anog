from message import Message
from multiLineMessage import MultiLineMessage

class Output(object):


    def __init__(self):
        self._toBeDisplayed={}

        self._toBeDisplayed['team']=MultiLineMessage()
        self._toBeDisplayed['content']=MultiLineMessage()
        self._toBeDisplayed['map']=MultiLineMessage()

    @property
    def toBeDisplayed(self):
        return self._toBeDisplayed

    def team(self, txt):
        '''
        if isinstance(txt,Message):
            self._toBeDisplayed['team'].append(txt)
        elif isinstance(txt, list):
            self._toBeDisplayed['team'].extend(txt)'''
        self._toBeDisplayed['team']+txt
        

    def content(self, txt):
        '''if isinstance(txt,Message):
            self._toBeDisplayed['content'].append(txt)
        elif isinstance(txt, list):
            self._toBeDisplayed['content'].extend(txt)'''
        self._toBeDisplayed['content']+txt

    def map(self, txt):
        '''if isinstance(txt,Message):
            self._toBeDisplayed['map'].append(txt)
        elif isinstance(txt, list):
            self._toBeDisplayed['map'].extend(txt)'''
        self._toBeDisplayed['map']+txt

    def reset(self):
        for key in self._toBeDisplayed:
            self._toBeDisplayed[key]=MultiLineMessage()
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