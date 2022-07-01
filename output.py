
from multiLineMessage import MultiLineMessage

class Output(object):


    def __init__(self):
        self._team=MultiLineMessage()
        self._content=MultiLineMessage()
        self._map=MultiLineMessage()

    @property
    def team(self):
        return self._team

    @property
    def content(self):
        return self._content

    @property
    def map(self):
        return self._map

    @team.setter
    def team(self, elem):
        self._team+elem

    @content.setter
    def content(self, elem):
        self._content+elem

    @map.setter
    def map(self, elem):
        self._map+elem


    def toBeDisplayed(self):
        temp={}
        temp['team']=self._team
        temp['content']=self._content
        temp['map']=self._map
        return temp

    def reset(self):
        self._team=MultiLineMessage()
        self._content=MultiLineMessage()
        self._map=MultiLineMessage()

  