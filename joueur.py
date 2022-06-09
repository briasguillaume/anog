
from utils import Utils
from equipage import Equipage
from pirate import Pirate
from world import World
from interactBDD import InteractBDD

class Joueur(object):

	debug=False


	def __init__(self, credentials):
		username=credentials[0]
		password=credentials[1]
		if self.existInDB(username):
			print("\n\n")
			while self.checkPassword(username, password)==False:
				print("Ton mot de passe semble faux, réessaye")
				password=self.askForPassword()
		else:
			print("User "+username+" enters the game, be careful or he will kick your ass!")
			self.createNewUser(username, password)
			Equipage([Pirate(1, True)]) #store it in db


		self._username= username
		self._equipage= self.getMyCrew()

		self._position= self.getMyLocation()

		self.showMenu()





	def showMenu(self):
		Utils.clear()
		print("Voici ton équipage:\n"+str(self._equipage))
		print("Vous êtes actuellement ici: "+str(self._position))
		World.showMap()
		nextIsland=World.next(self._position.name)
		if nextIsland==None:
			print("GG t'es devenu le roi des pirates")
			return None

		self._position=nextIsland
		self._equipage.regenerateHealth()
		Utils.fight(self._equipage, self._position.pirates)
		if self._equipage.availableToFight:
			self.recrutement(5)
		else:
			#delete everything from db
			self._equipage= self.getMyCrew()
			self._position= self.getMyLocation()
			playagain= input("Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n \n" )
			while playagain!="y":
				playagain= input("Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n \n" )
			


		Utils.clear()
		self.showMenu()




	def recrutement(self, number):
		pirates=[]
		print("Des pirates sont disponibles au recrutement.\n")
		for i in range(0,number):
			pirate=Pirate(self._position.level)
			pirates.append(pirate)
			print("Choix "+str(i)+": "+str(pirate))
		value = int(input("Lequel voulez-vous recruter?\n"))
		if value<number:
			self._equipage.newFighter(pirates[value])
		



	@property
	def position(self):
		return self._position









	def existInDB(self, username):
		if Joueur.debug:
			return True
		else:
			return InteractBDD.existInDB(username)


	def createNewUser(self, username, password):
		if Joueur.debug:
			pass
		else:
			InteractBDD.createUser(username, password)


	def checkPassword(self, username, password):
		if Joueur.debug:
			return True
		else:
			InteractBDD.checkPassword(username, password)


	def getMyCrew(self):
		if Joueur.debug:
			return Equipage([Pirate(1, True)])
		else:
			InteractBDD.getMyCrew(self._username)


	def getMyLocation(self):
		if Joueur.debug:
			return World.carte()[0].islands[0]
		else:
			InteractBDD.getMyLocation(self._username)
	

















