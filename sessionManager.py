from menu import Menu
from interactBDD import InteractBDD
from multiLineMessage import MultiLineMessage
from joueur import Joueur

import hashlib


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
        
        
    def session(self, username, auth, user_input):
        if self.sanitization(user_input):
            if username in self._players:
                if auth:
                    return [self.getMenu(username).showMenu(user_input), auth] # utilisateur connu et déjà connecté
                else: # utilisateur a priori connu mais authentification necessaire
                    return self.instanciateJoueur(username, user_input[1])
                    
            else: # utilisateur inconnu
                joueur = Joueur(username, user_input[1])
                menu = self.newSession(username)
                menu.joueur = joueur
                return [menu.showMenu(), True]
        else:
            output = MultiLineMessage()
            output+ "Caractères non-autorisés entrés"
            return [output, False]
        
    def getMenu(self, username):
        return self._players[username]
        
    def instanciateJoueur(self, username, password):
        InteractBDD.cleanUpDB()

        # https://docs.python.org/fr/3/library/hashlib.html
        password=hashlib.blake2b(password.encode('utf-8')).hexdigest()
        try:
            password=password[0:240]
        except:
            pass

        if InteractBDD.existInDB(username):
            if not InteractBDD.checkPassword(username, password):
                output= MultiLineMessage()
                output.content+ "Mauvais mot de passe, réessaie."
                return [output, False] # password was wrong
				
        return [self.getMenu(username).showMenu(), True]

        
    def sanitization(self, user_input):
        forbiddenCharacters=["'", "\"", "\\", "&", "~", "{", "(", "[", "-", "|", "`", "_", "ç", "^", "à", "@", ")", "]", "=", "}", "+", "$", "£", "¤", "*", "µ", "ù", "%", "!", "§", ":", "/", ";", ".", ",", "?", "<", ">", "²"]
        if len(user_input)==0 or user_input=="": # empty input
            return False

        for elem in user_input:
            if len(elem)>=15: # max 15 characters
                return False
                
            for char in forbiddenCharacters: # no special characters
                if char in elem:
                    return False
        return True

        
        















