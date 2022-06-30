import random
import numpy as np
import os

from fruitdemon import FruitDemon
from fruitdemon import FruitFactory
from pirate import Pirate


import json
from collections import namedtuple
from json import JSONEncoder

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(entry1, entry2):		
		txt=""
		first=random.randint(1,2)
		turnsCount=0
		while entry1.availableToFight and entry2.availableToFight:
			txt=txt+"Tour "+str(turnsCount)+":\n"
			txt=txt+Utils.phraseDeCombat(entry2, entry1)
			Utils.updateStatus(entry1)
			txt=txt+Utils.phraseDeCombat(entry1, entry2)
			Utils.updateStatus(entry2)
			txt=txt+"\n"
			turnsCount+=1
		if entry1.availableToFight:
			entry1.increaseCrewLevel()
			txt=txt+Utils.phraseDeVictoire(entry1)
		else:
			entry2.increaseCrewLevel()
			txt=txt+Utils.phraseDeVictoire(entry2)
		return txt+"\n"


	@staticmethod
	def increaseCrewLevel(entry):
		if entry.isinstance()=="Joueur":
			entry.equipage.increaseCrewLevel()
		elif entry.isinstance()=="Equipage":
			entry.increaseCrewLevel()


	@staticmethod
	def updateStatus(entry):
		if entry.isinstance()=="Joueur":
			entry.equipage.updateStatus()
		elif entry.isinstance()=="Equipage":
			entry.updateStatus()


	@staticmethod
	def phraseDeCombat(entryA, entryB):
		txt=""
		if entryA.isinstance()=="Joueur":
			if entryB.isinstance()=="Joueur":
				txt=txt+"L'équipage de "+entryA.username+" attaque:"+entryA.equipage.attaque(entryB.equipage)+"\n"
			elif entryB.isinstance()=="Equipage":
				txt=txt+"L'équipage de "+entryA.username+" attaque:"+entryA.equipage.attaque(entryB)+"\n"
		elif entryA.isinstance()=="Equipage":
			if entryB.isinstance()=="Joueur":
				txt=txt+"Tour de l'équipage PNJ d'attaquer:"+entryA.attaque(entryB.equipage)+"\n"
			elif entryB.isinstance()=="Equipage":
				txt=txt+"Tour de l'équipage PNJ d'attaquer:"+entryA.attaque(entryB)+"\n"
			
		return txt
		

	@staticmethod
	def phraseDeVictoire(entry):
		txt=""
		if entry.isinstance()=="Joueur":
			txt=txt+"L'équipage de "+entry.username+" remporte le combat, ils remportent tous un niveau:\n"+str(entry.equipage)+"\n"
		elif entry.isinstance()=="Equipage":
			txt=txt+"L'équipage PNJ remporte le combat! \n"
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
		


	#_________________________________LOADING DYNAMICALLY____________________________

	@staticmethod
	def decode(dict):
		tuple=namedtuple('Metamorph', dict.keys())(*dict.values())
		if tuple.type=="Pirate":
			obj= Pirate(tuple.level)
			obj.name=tuple.name
			obj.qualite=tuple.qualite
			obj.fruit=tuple.fruit
		elif tuple.type=="FruitDemon":
			obj= FruitFactory.giveThatFruit(tuple.name)
		else:
			obj=None
		return obj


	@staticmethod
	def load(obj):
		return json.loads(obj, object_hook=Utils.decode)






