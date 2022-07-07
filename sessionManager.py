from menu import Menu
from interactBDD import InteractBDD
from multiLineMessage import MultiLineMessage
from joueur import Joueur
from utils import Utils


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
    
    
    
    def newSession(self, username, password):
        joueur = Joueur(username, password)
        menu = Menu()
        menu.joueur = joueur
        return menu

        
    def chargeProfile(self, username):
        joueur = Joueur(username)
        menu = Menu()
        menu.joueur = joueur
        return menu
        
        
    def session(self, username, auth, user_input):
        if self.sanitization(user_input):
            if auth:
                return [self.chargeProfile(username).showMenu(), True]
            else:
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
        
        
    def checkPassword(self, username, password):
        password=Utils.hashPassword(password)

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


        
        















