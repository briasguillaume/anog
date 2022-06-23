class SessionManager(object):
    
    
    def __init__(self):
        self._playersID={}
        self._menusID={}
        
    def newSession(self, username):
        newid=self.maxID()+1
        self._playersID[username]=newid
        self._menusID[newid]=m.Menu()
        return self._menusID[newid]
        
        
    def session(self, username):
        if username in self._playersID:
            return self.getMenu(username)
        else:
            return self.newSession(username)
        
    def getMenu(self, username):
        return self._menusID[self._playersID[username]]
    
    
    def maxID(self):
        return max(self._playersID.values())