import random
import numpy as np
import os

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
		if equipage1.availableToFight:
			equipage1.increaseCrewLevel()
			print("Cet équipage remporte le combat, ils remportent tous un niveau:\n"+str(equipage1)+"\n")
		else:
			equipage2.increaseCrewLevel()
			print("Cet équipage remporte le combat:\n"+str(equipage2)+"\nIls remportent tous un niveau!\n")



	@staticmethod
	def shuffle(pirates):
		places=np.arange(0,len(pirates))
		random.shuffle(places)
		shuffledList=[]
		for place in places:
			shuffledList.append(pirates[place])
		return shuffledList


	@staticmethod
	def askForCredentials():
		username= input("Can you give your username?")
		password= input("Now we need you to give your password.")
		return [username, password]

	@staticmethod
	def askForPassword():
		password= input("Now we need you to give your password.")
		return password




	@staticmethod
	def clear():
		os.system('cls')
		




					







