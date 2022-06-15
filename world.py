

from island import Island
from stage import Stage

class World(object):

	debug=False

	#store it in db
	world=[Stage([Island("Karugarner", 0,0)],0),
			Stage([Island("Cupcake", 1, 3), Island("Bonbons", 2, 1)],1),
			Stage([Island("Bottle", 2, 3), Island("String", 3, 2), Island("Slip", 4, 1)],2),
			Stage([Island("Diplodocus", 3 , 3), Island("Fridge", 4, 2), Island("Montgolfiere", 5, 1)],3),
			Stage([Island("Picmin", 4 , 3)],4),
			Stage([Island("PoissonRouge", 5 , 3), Island("Gateau", 7, 1)],5),
			Stage([Island("Bouton", 6 , 3), Island("Fesse", 8, 1)],6)
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
			"Fesse":6
			}


	@staticmethod
	def carte():
		return World.world

	@staticmethod
	def next(currentIslandName, choix=0):
		if World.debug:
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
		else:
			maxIndex=len(World.world)-1
			index=World.avancee[currentIslandName]+1
			if index<=maxIndex:
				stage=World.world[index]
				
				try:
					island=stage.islands[choix]
				except:
					island=stage.islands[0]
				island.regenerate()
			else:
				return None
			return [island, str(stage)]



	@staticmethod
	def has(name):
		for stage in World.world:
			for island in stage.islands:
				if island.name==name:
					return True
		return False

	@staticmethod
	def showMap():
		if World.debug:
			txt=""
			for stage in World.world:
				txt=txt+"------------------------------------------------------------\n" #60
				#1 20 20
				#2 5 55 55 5
				spaceLength=60/(len(stage.islands)+1) -10
				for island in stage.islands:
					for i in range(int(spaceLength)):
						txt=txt+" "
					txt=txt+"|"+island.name+"|"
					for i in range(int(spaceLength)):
						txt=txt+" "
				txt=txt+"\n"
			print(txt)
		else:
			txt=""
			for stage in World.world:
				txt=txt+"------------------------------------------------------------ <br>" #60
				#1 20 20
				#2 5 55 55 5
				spaceLength=60/(len(stage.islands)+1) -10
				for island in stage.islands:
					for i in range(int(spaceLength)):
						txt=txt+"&nbsp;"
					txt=txt+"|"+island.name+"|"
					for i in range(int(spaceLength)):
						txt=txt+"&nbsp;"
				txt=txt+"<br>"
			return txt

















