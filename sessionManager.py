from menu import Menu

class SessionManagerMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SessionManager(metaclass=SessionManagerMeta):
    
    
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
    
    