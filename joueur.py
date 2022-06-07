
from utils import Utils
from equipage import Equipage
from pirate import Pirate
from world import World


class Joueur(object):




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

		nextIsland=World.next(self._position.name)
		if nextIsland==None:
			print("GG t'es devenu le roi des pirates")
			return None

		print("La prochaine ile est "+str(nextIsland)+"\n")
		bool = input("Vous voulez y aller? y/n\n")
		while bool!="y":
			bool = input("Vous voulez y aller? y/n\n")

		self._position=nextIsland
		self._equipage.regenerateHealth()
		Utils.fight(self._equipage, self._position.pirates)
		if self._equipage.availableToFight:
			pirate=Pirate(self._position.level)
			print("Le pirate "+pirate.name+" est disponible au recrutement.\n")
			print(pirate)
			bool = input("Voulez-vous le recruter? y/n\n")
			if bool=="y":
				self._equipage.newFighter(pirate)
		else:
			#delete everything from db
			self._equipage= self.getMyCrew()
			self._position= self.getMyLocation()
			playagain= input("Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n \n" )
			while playagain!="y":
				playagain= input("Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n \n" )
			


		Utils.clear()
		self.showMenu()







	@property
	def position(self):
		return self._position









	def existInDB(self, username):
		return True


	def createNewUser(self, username, password):
		pass


	def checkPassword(self, username, password):
		return True


	def getMyCrew(self):
		return Equipage([Pirate(1, True)])
		# get it from db


	def getMyLocation(self):
		return World.carte()[0]
		#get it from db

















