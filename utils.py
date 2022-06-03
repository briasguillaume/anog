import random
import numpy as np

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(equipage1, equipage2):
		first=random.randint(1,2)
		turnsCount=0
		while equipage1.availableToFight and equipage2.availableToFight:
			print("Tour "+str(turnsCount)+":")
			print("Equipage 2:"+equipage2.attaque(equipage1))
			print("Equipage 1:"+equipage1.attaque(equipage2)+"\n")
			turnsCount+=1


	@staticmethod
	def shuffle(pirates):
		places=np.arange(0,len(pirates))
		random.shuffle(places)
		shuffledList=[]
		for place in places:
			shuffledList.append(pirates[place])
		return shuffledList








					







