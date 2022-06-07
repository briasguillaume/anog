

from island import Island
from stage import Stage

class World(object):


	#store it in db
	world=[Stage([Island("Karugarner", 0,0)],0),
			Stage([Island("Cupcake", 1, 3), Island("Bonbons", 1, 3)],1),
			Stage([Island("Bottle", 2, 3)],2),
			Stage([Island("Diplodocus", 3 , 3)],3),
			Stage([Island("Picmin", 4 , 3)],4),
			Stage([Island("PoissonRouge", 5 , 3)],5),
			Stage([Island("Bouton", 6 , 3)],6)
			]

	avancee={"Karugarner":0,
			"Cupcake":1,
			"Bonbons":1,
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
			stage=World.world[index]
			if len(stage.islands)==1:
				island=stage.islands[0]
				island.regenerate()
				return island
			print(stage)
			choix=int(input("Dans quelle ile veux-tu aller?"))
			while choix>=len(stage.islands):
				choix=input("Dans quelle ile veux-tu aller?")
			island=stage.islands[choix]
			island.regenerate()
		else:
			return None
		return island



	def __str__(self):
		txt=""


		return txt

















