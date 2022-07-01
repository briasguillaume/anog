from message import Message
from multiLineMessage import MultiLineMessage

class Output(object):


    def __init__(self):
        self._toBeDisplayed={}

        
        self._team=MultiLineMessage()
        self._content=MultiLineMessage()
        self._map=MultiLineMessage()

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
        temp={}
        temp['team']=self._team
        temp['content']=self._content
        temp['map']=self._map
        return temp

    def reset(self):
        for key in self._toBeDisplayed:
            self._toBeDisplayed[key]=MultiLineMessage()

  