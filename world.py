

from island import Island

class World(object):


	#store it in db
	world=[Island("Karugarner", 0,0),
			Island("Cupcake", 1, 5),
			Island("Bottle", 2, 3)
			]

	avancee={"Karugarner":0,
			"Cupcake":1,
			"Bottle":2
			}


	def __init__(self):
		print("Bonjour je suis la carte.")

	@staticmethod
	def carte():
		return World.world

	@staticmethod
	def next(currentIslandName):
		island=World.world[World.avancee[currentIslandName]+1]
		island.regenerate()
		return island