
from utils import Utils
from equipage import Equipage
from pirate import Pirate
from island import World


class Joueur(object):




	def __init__(self, credentials):
		username=credentials[0]
		password=credentials[1]
		if self.existInDB(username):
			print(username+" comes back to kick your ass!")
			while self.checkPassword(username, password)==False:
				password=self.askForPassword()
		else:
			print("User "+username+" enters the game, be careful or he will kick your ass!")
			self.createNewUser(username, password)
			Equipage([Pirate(1, True)]) #store it in db


		self._username= username
		self._equipage= self.getMyCrew()

		self._position= self.getMyLocation()





	def showMenu(self):

		print(self._equipage)
		print(self._position)

		print("La prochaine ile est \n")
		print(World.next())
		bool = input("Vous voulez y aller? y/n")
		while bool!="y":
			bool = input("Vous voulez y aller? y/n")











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