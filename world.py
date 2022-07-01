

from island import Island
from stage import Stage
from message import Message

class World(object):
	#store it in db
	world=[Stage([Island("Karugarner", 0,0)]),
			Stage([Island("Cupcake", 1, 3), Island("Bonbons", 2, 1)]),
			Stage([Island("Bottle", 2, 3), Island("String", 3, 2), Island("Slip", 4, 1)]),
			Stage([Island("Diplodocus", 3 , 3), Island("Fridge", 4, 2), Island("Montgolfiere", 5, 1)]),
			Stage([Island("Picmin", 4 , 3)]),
			Stage([Island("PoissonRouge", 5 , 3), Island("Gateau", 7, 1)]),
			Stage([Island("Bouton", 6 , 3), Island("Fesse", 8, 1)]),
			Stage([Island("Shinsekai", 20 , 1)]),
			Stage([Island("Marguerite", 20 , 3), Island("Tulipe", 30, 1)]),
			Stage([Island("Serpent", 20 , 6), Island("Singe", 30, 3), Island("Chien", 40, 1), Island("Dragon", 50, 1)]),
			Stage([Island("Chaise", 25 , 6), Island("portefeuille", 35, 6), Island("Table", 45, 6), Island("Escalier", 55, 6), Island("Fourchette", 65, 6)],),
			Stage([Island("Voiture", 70 , 3), Island("Velo", 80, 3), Island("Train", 85, 3), Island("Avion", 90, 3)],),
			Stage([Island("Etoile", 150 , 1)])
			]

	avancee={"Karugarner":0,
			"Cupcake":1,
			"Bonbons":1,
			"Bottle":2,
			"String":2,
			"Slip":2,
			"Diplodocus":3,
			"Fridge":3,
			"Montgolfiere":3,
			"Picmin":4,
			"PoissonRouge":5,
			"Gateau":5,
			"Bouton":6,
			"Fesse":6,
			"Shinsekai":7,
			"Marguerite":8,
			"Tulipe":8,
			"Serpent":9,
			"Singe":9,
			"Chien":9,
			"Dragon":9,
			"Chaise":10,
			"portefeuille":10,
			"Table":10,
			"Escalier":10,
			"Fourchette":10,
			"Voiture":11,
			"Velo":11,
			"Train":11,
			"Avion":11,
			"Etoile":12
			}


	@staticmethod
	def carte():
		return World.world

	@staticmethod
	def next(currentIslandName, choix=0):
		choix=int(choix)
		availableIslands=World.availableIslands(currentIslandName)
		World.getIsland(currentIslandName).regenerate()
		if choix<=len(availableIslands)-1 and choix>=0: # TODO verify user input

			try:
				island=availableIslands[int(choix)]
			except:
				island=availableIslands[0]
		else:
			return None
		return island


	@staticmethod
	def getIsland(currentIslandName):
		index=World.avancee[currentIslandName]
		stage=World.world[index]
		for island in stage.islands:
			if island.name==currentIslandName:
				return island

	@staticmethod
	def availableIslands(currentIslandName):
		maxIndex=len(World.world)-1
		minIndex=1
		index=World.avancee[currentIslandName]
		availableStages=[]
		for i in range(index-1,index+2): #it takes values index-1, index, index+1
			if i>=minIndex and i<=maxIndex:
				availableStages.append(World.world[i])
		availableIslands=[]
		for stage in availableStages:
			for island in stage.islands:
				if island.name!=currentIslandName:
					availableIslands.append(island)
		return availableIslands

	@staticmethod
	def getNextStage(currentIslandName):
		availableIslands=World.availableIslands(currentIslandName)
		return Stage(availableIslands).asMessageArray()





	@staticmethod
	def has(name):
		for stage in World.world:
			for island in stage.islands:
				if island.name==name:
					return True
		return False

	@staticmethod
	def showMap(currentIslandName):
		array=[]
		for stage in World.world:
			array.append(Message('------------------------------------------------------------')) #60
			#1 20 20
			#2 5 55 55 5
			spaceLength=60/(len(stage.islands)+1) -10
			txt=""
			for island in stage.islands:
				for i in range(int(spaceLength)):
					txt=txt+" "
				txt=txt+'|'
				if island.name!=currentIslandName:
					txt=txt+island.name
				else:
					txt=txt+island.name
				txt=txt+'|'
				for i in range(int(spaceLength)):
					txt=txt+" "  #&nbsp; est un espace
			array.append(Message(txt))
		return array

















