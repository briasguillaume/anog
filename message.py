



class Message(object):

    def __init__(self, texte, gras=False, couleur=[0, 0, 0, 0.16]):
        self._gras=gras
        self._couleur=couleur
        self._texte=texte



    @property
    def gras(self):
        return self._gras

        

    @property
    def couleur(self):
        return self._couleur

        

    @property
    def texte(self):
        return self._texte

        

    @gras.setter
    def gras(self, gras):
        self._gras=gras

        

    @couleur.setter
    def couleur(self, couleur):
        self._couleur=couleur

        

    @texte.setter
    def texte(self, texte):
        self._texte=texte

    def __add__(self, message):
        self._texte=self._texte+message.texte
        






'''

class Message(object):

    def __init__(self, texte, gras=False, couleur=[0, 0, 0, 0.16]):
        message={}
        message['gras']=gras
        message['couleur']=couleur
        message['texte']=texte
        self._manyMessages=[message]

    @property
    def manyMessages(self):
        return self._manyMessages
        
    def __add__(self, message):
        self._manyMessages=self._manyMessages.append(message)

'''















