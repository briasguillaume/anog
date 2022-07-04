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
        
    def newSession(self, username, password):
        joueur = Joueur(username, password)
        self._players[username]=Menu()
        self._players[username].joueur = joueur
        return self._players[username]
        
        
    def session(self, username, auth, user_input):
        if self.sanitization(user_input):
            if username in self._players:
                if auth:
                    return [self.getMenu(username).showMenu(user_input), auth] # utilisateur connu et déjà connecté
                else: # utilisateur a priori connu mais authentification necessaire
                    [known, auth] = self.checkPassword(username, user_input[1])
                    if auth:
                        return [self.getMenu(username).showMenu(), True]

                    else:
                        output= MultiLineMessage()
                        output+ "Mauvais mot de passe, réessaie."
                        return [output, False]
            else: # utilisateur inconnu car profil pas chargé ou nouveau joueur
                [known, auth] = self.checkPassword(username, user_input[1])
                if known and auth: # connu et bon mdp
                    return [self.chargeProfile(username).showMenu(), True]
                elif known: # connu mais mauvais mdp
                    output= MultiLineMessage()
                    output+ "Mauvais mot de passe, réessaie."
                    return [output, False]
                else: # inconnu et nouveau mdp
                    return [self.newSession(username, user_input[1]).showMenu(), True]
               
        else:
            output = MultiLineMessage()
            output+ "Caractères non-autorisés entrés"
            return [output, False]
        
    def getMenu(self, username):
        return self._players[username]
        
    def checkPassword(self, username, password):
        InteractBDD.cleanUpDB()

        # https://docs.python.org/fr/3/library/hashlib.html
        password=hashlib.blake2b(password.encode('utf-8')).hexdigest()
        try:
            password=password[0:240]
        except:
            pass

        if InteractBDD.existInDB(username):
            if not InteractBDD.checkPassword(username, password):
                return [True, False] # password was wrong
            return [True, True] # password was correct
				
        return [False , False]# username not known

        
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

    def chargeProfile(self, username):
        joueur = Joueur(username)
        self._players[username]=Menu()
        self._players[username].joueur = joueur
        return self._players[username]

        
        















