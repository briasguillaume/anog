

from island import Island

class World(object):


	#store it in db
	world=[Island("Karugarner", 0,0),
			Island("Cupcake", 1, 3),
			Island("Bottle", 2, 3),
			Island("Diplodocus", 3 , 3),
			Island("Picmin", 4 , 3),
			Island("PoissonRouge", 5 , 3),
			Island("Bouton", 6 , 3)
			]

	avancee={"Karugarner":0,
			"Cupcake":1,
			"Bottle":2,
			"Diplodocus":3,
			"Picmin":4,
			"PoissonRouge":5,
			"Bouton":6
			}


	def __init__(self):
		print("Bonjour je suis la carte.")

	@staticmethod
	def carte():
		return World.world

	@staticmethod
	def next(currentIslandName):
		maxIndex=len(World.world)-1
		index=World.avancee[currentIslandName]+1
		if index<=maxIndex:
			island=World.world[index]
			island.regenerate()
		else:
			return None
		return island



	def __str__(self):
		txt=""


		return txt

















		