
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
			
			
		else:
			if self.existInDB(username):
				if not InteractBDD.checkPassword:
					# for testing purpose
					self._username= username
					self._equipage= self.getMyCrew()
					self._position= self.getMyLocation()
					#
					return "Invalid password"
					# TODO handle wrong passwords
			else:
				self.createNewUser(username, password)
				InteractBDD.setMyCrew(username, World.carte()[0].islands[0].name, [Pirate(1, True)]) 
			self._username= username
			self._equipage= self.getMyCrew()
			self._position= self.getMyLocation()
			

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
			txt="Voici ton équipage:<br>"+str(self._equipage)+"<br>"
			txt=txt+"Vous êtes actuellement ici: "+str(self._position)+"<br>"
			txt=txt+World.showMap()
			
			txt=txt+"Dans quelle ile veux-tu aller maintenant? <br>"
			return txt


	def goingToNextIsland(self, value):
		self._position=World.next(self._position.name, value)
		#if nextIsland==None:
		#	return "GG t'es devenu le roi des pirates"
		# TODO HANDLE END OF THE MAP
		self._equipage.regenerateHealth()
		txt=Utils.fight(self._equipage, self._position.pirates)
		''' TODO handle death
		if self._equipage.availableToFight:
			self.recrutement(5)
		else:
			#delete everything from db
			self._equipage= self.getMyCrew()
			self._position= self.getMyLocation()
			txt=txt+"Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n <br>"
		'''
		return txt

	def recrutement(self, number, pirates=[], value=0):
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
			if int(value)<number:
				self._equipage.newFighter(pirates[int(value)])
			return self.showMenu()


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
			return InteractBDD.createUser(username, password)


	def checkPassword(self, username, password):
		if Joueur.debug:
			return True
		else:
			return InteractBDD.checkPassword(username, password)


	def getMyCrew(self):
		if Joueur.debug:
			return Equipage([Pirate(1, True)])
		else:
			return InteractBDD.getMyCrew(self._username)


	def getMyLocation(self):
		if Joueur.debug:
			return World.carte()[0].islands[0]
		else:
			return InteractBDD.getMyLocation(self._username)
	

















