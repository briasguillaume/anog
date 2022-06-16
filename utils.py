import random
import numpy as np
import os

from fruitdemon import FruitDemon
from pirate import Pirate


class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	debug=False

	@staticmethod
	def fight(entry1, entry2):
		if entry1.isinstance()=="Joueur":
			equipage1=entry1.team
		elif entry1.isinstance()=="Equipage":
			equipage1=entry1 

		if entry2.isinstance()=="Joueur":
			equipage2=entry2.team
		elif entry2.isinstance()=="Equipage":
			equipage2=entry2 

		if Utils.debug:
			first=random.randint(1,2)
			# TODO HANDLE FIRST
			turnsCount=0
			while equipage1.availableToFight and equipage2.availableToFight:
				print("Tour "+str(turnsCount)+":")
				print("Equipage 2:"+equipage2.attaque(equipage1))
				joueur1.cleanUpDeadPirates()
				equipage1.updateStatus()
				print("Equipage 1:"+equipage1.attaque(equipage2))
				joueur2.cleanUpDeadPirates()
				equipage2.updateStatus()
				print("\n")
				turnsCount+=1
			if equipage1.availableToFight:
				equipage1.increaseCrewLevel()
				print(joueur1.username+" remporte le combat, ils remportent tous un niveau:\n"+str(equipage1)+"\n")
			else:
				equipage2.increaseCrewLevel()
				print(joueur2.username+" remporte le combat:\n"+str(equipage2)+"\nIls remportent tous un niveau!\n")
		else:
			txt=""
			first=random.randint(1,2)
			turnsCount=0
			while equipage1.availableToFight and equipage2.availableToFight:
				txt=txt+"Tour "+str(turnsCount)+":<br>"
				txt=txt+Utils.phraseDeCombat(equipage2, equipage1)
				equipage1.updateStatus()
				txt=txt+Utils.phraseDeCombat(equipage1, equipage2)
				equipage2.updateStatus()
				txt=txt+"<br>"
				turnsCount+=1
			if equipage1.availableToFight:
				equipage1.increaseCrewLevel()
				# TODO interactBDD.increaseCrewLevel(joueur1.username)
				txt=txt+Utils.phraseDeVictoire(entry1)
			else:
				equipage2.increaseCrewLevel()
				txt=txt+Utils.phraseDeVictoire(entry2)
			return txt


	@staticmethod
	def phraseDeCombat(equipageA, equipageB):
		txt=""
		if equipageA.isinstance()=="Joueur":
			txt=txt+"L'équipage de "+equipageA.username+" attaque:"+equipageA.attaque(equipageB)+"<br>"
		elif equipageA.isinstance()=="Equipage":
			txt=txt+"Equipage 1:"+equipageA.attaque(equipageB)+"<br>"
		return txt
		

	@staticmethod
	def phraseDeVictoire(entry):
		txt=""
		if entry.isinstance()=="Joueur":
			txt=txt+"L'équipage de "+entry.username+" remporte le combat, ils remportent tous un niveau:<br>"+str(entry.team)+"<br>"
		elif entry.isinstance()=="Equipage":
			txt=txt+"Cet équipage remporte le combat, ils remportent tous un niveau:<br>"+str(entry)+"<br>"
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
		


	'''
	@staticmethod
	def decode(dict):
		tuple=namedtuple('Metamorph', dict.keys())(*dict.values())
		if tuple.type=="Pirate":
			obj= Pirate(tuple.level)
			obj.name=tuple.name
			obj.qualite=tuple.qualite
			obj.fruit=tuple.fruit
		elif tuple.type=="FruitDemon":
			obj= FruitDemon(tuple.name, tuple.power)
		else:
			obj=None
		return obj'''

	'''
	@staticmethod
	def decode(dict):
		return namedtuple('Metamorph', dict.keys())(*dict.values())
	# TODO handle it with metaclasses'''


	'''
	@staticmethod
	def load(obj):
		return json.loads(obj, object_hook=Utils.decode)'''






