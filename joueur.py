
from utils import Utils
from equipage import Equipage
from pirate import Pirate
from world import World
from interactBDD import InteractBDD

class Joueur(object):

	debug=False


	def __init__(self, username, password):
		if Joueur.debug:
			self._username= username
			self._equipage= self.getMyCrew()

			self._position= self.getMyLocation()

			self.showMenu()
		else:
			if self.existInDB(username):
				if not InteractBDD.checkPassword:
					return "Invalid password"
					# TODO handle wrong passwords

			else:
				self.createNewUser(username, password)
				InteractBDD.setMyCrew(username, World.carte()[0].islands[0].name, [Pirate(1, True)]) 
			


			self._username= username
			
			self._equipage= self.getMyCrew()

			self._position= self.getMyLocation()

			self.showMenu()






	def showMenu(self):
		if Joueur.debug:
			Utils.clear()
			print("Voici ton équipage:\n"+str(self._equipage)+"\n")
			print("Vous êtes actuellement ici: "+str(self._position)+"\n")
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

		else:
			txt="Voici ton équipage:\n"+str(self._equipage)+"<br>"
			txt=txt+"Vous êtes actuellement ici: "+str(self._position)+"<br>"
			txt=txt+World.showMap()
			nextIsland=World.next(self._position.name)
			if nextIsland==None:
				return "GG t'es devenu le roi des pirates"

			self._position=nextIsland
			self._equipage.regenerateHealth()
			Utils.fight(self._equipage, self._position.pirates)
			if self._equipage.availableToFight:
				self.recrutement(5)
			else:
				#delete everything from db
				self._equipage= self.getMyCrew()
				self._position= self.getMyLocation()
				txt=txt+"Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n <br>"
				
				#TODO HANDLE INPUT

			return txt




	def recrutement(self, number):
		if Joueur.debug:
			pirates=[]
			print("Des pirates sont disponibles au recrutement.\n")
			for i in range(0,number):
				pirate=Pirate(self._position.level)
				pirates.append(pirate)
				print("Choix "+str(i)+": "+str(pirate))
			value = int(input("Lequel voulez-vous recruter?\n"))
			if value<number:
				self._equipage.newFighter(pirates[value])
		else:
			pirates=[]
			txt=""
			txt=txt+"Des pirates sont disponibles au recrutement. <br>"
			for i in range(0,number):
				pirate=Pirate(self._position.level)
				pirates.append(pirate)
				txt=txt+"Choix "+str(i)+": "+str(pirate)

			txt=txt+"Lequel voulez-vous recruter?<br>"
			value = int(input("Lequel voulez-vous recruter?<br>"))
# TODO HANDLE INPUT
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
	

















