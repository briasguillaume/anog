from menu import Menu

class SessionManager(object):
    
    
    def __init__(self):
        self._players={}
        
    def newSession(self, username):
        self._players[username]=Menu()
        return self._players[username]
        
        
    def session(self, username):
        if username in self._players:
            return self.getMenu(username)
        else:
            return self.newSession(username)
        
    def getMenu(self, username):
        return self._players[username]
    
    