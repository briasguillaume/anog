from message import Message
from multiLineMessage import MultiLineMessage

class Output(object):


    def __init__(self):
        self._toBeDisplayed={}

        self._toBeDisplayed['team']=MultiLineMessage()
        self._toBeDisplayed['content']=MultiLineMessage()
        self._toBeDisplayed['map']=MultiLineMessage()

    @property
    def team(self):
        return self._toBeDisplayed['team']

    @property
    def content(self):
        return self._toBeDisplayed['content']

    @property
    def map(self):
        return self._toBeDisplayed['map']

    @property
    def toBeDisplayed(self):
        return self._toBeDisplayed

    def reset(self):
        for key in self._toBeDisplayed:
            self._toBeDisplayed[key]=MultiLineMessage()

  