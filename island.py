
from equipage import Equipage
from pirate import Pirate


class World(object):


	#store it in db
	world=[Island("Karugarner", 0,0),
			Island("Cupcake", 1, 5),
			Island("Bottle", 2, 3)
			]

	avancee={"Karugarner":0,
			"Cupcake":1
			"Bottle":2
			}


	def __init__(self):
		print("Bonjour je suis la carte.")

	@staticmethod
	def carte():
		return World.world

	@staticmethod
	def next(currentIslandName):
		return World.world[avancee[currentIslandName]+1]



class Island(object):


	def __init__(self, name, level, ennemies):
		self._name=name
		self._level=level
		self._pirates=Equipage(generateEnnemies(level, ennemies))



	def generateEnnemies(self, level, ennemies):
		pirates=[]
		for i in range(ennemies):
			pirates.append(Pirate(level))
		return pirates


	def __str__(self):
		return "Vous êtes actuellement sur l'ile "+self._name+", il y a "+self._pirates.numberOfPirates+" pirates de niveau "+self._level+".\n"



	@property
	def name(self):
		return self._name



	@property
	def level(self):
		return self._level



	@property
	def pirates(self):
		return self._pirates