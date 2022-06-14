import random
import numpy as np
import os



import json
from collections import namedtuple
from json import JSONEncoder

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	debug=False

	@staticmethod
	def fight(equipage1, equipage2):
		if Utils.debug:
			first=random.randint(1,2)
			# TODO HANDLE FIRST
			turnsCount=0
			while equipage1.availableToFight and equipage2.availableToFight:
				print("Tour "+str(turnsCount)+":")
				print("Equipage 2:"+equipage2.attaque(equipage1))
				equipage1.updateStatus()
				print("Equipage 1:"+equipage1.attaque(equipage2))
				equipage2.updateStatus()
				print("\n")
				turnsCount+=1
			if equipage1.availableToFight:
				equipage1.increaseCrewLevel()
				print("Cet équipage remporte le combat, ils remportent tous un niveau:\n"+str(equipage1)+"\n")
			else:
				equipage2.increaseCrewLevel()
				print("Cet équipage remporte le combat:\n"+str(equipage2)+"\nIls remportent tous un niveau!\n")
		else:
			txt=""
			first=random.randint(1,2)
			turnsCount=0
			while equipage1.availableToFight and equipage2.availableToFight:
				txt=txt+"Tour "+str(turnsCount)+":<br>"
				txt=txt+"Equipage 2:"+equipage2.attaque(equipage1)+"<br>"
				equipage1.updateStatus()
				txt=txt+"Equipage 1:"+equipage1.attaque(equipage2)+"<br>"
				equipage2.updateStatus()
				txt=txt+"<br>"
				turnsCount+=1
			if equipage1.availableToFight:
				equipage1.increaseCrewLevel()
				txt=txt+"Cet équipage remporte le combat, ils remportent tous un niveau:<br>"+str(equipage1)+"<br>"
			else:
				equipage2.increaseCrewLevel()
				txt=txt+"Cet équipage remporte le combat:<br>"+str(equipage2)+"<br>Ils remportent tous un niveau!<br>"
			return txt


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


	@staticmethod
	def removeElement(array, index):
		temp=[]
		count=0
		for elem in array:
			if count!=index:
				temp.append(elem)
			count+=1
		return temp
		



	@staticmethod
	def decode(dict):
		return namedtuple('X', dict.keys())(*dict.values())
	# TODO handle it with metaclasses

	@staticmethod
	def load(obj):
		return json.loads(obj, object_hook=Utils.decode)






