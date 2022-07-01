import random
import numpy as np
import os

from fruitdemon import FruitDemon
from fruitdemon import FruitFactory
from pirate import Pirate
from message import Message

import json
from collections import namedtuple
from json import JSONEncoder

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(entry1, entry2):		
		array=[]
		first=random.randint(1,2)
		turnsCount=0
		while entry1.availableToFight and entry2.availableToFight:
			array.append(Message("Tour "+str(turnsCount), True))
			if first==1:
				array.append(Utils.phraseDeCombat(entry2, entry1))
				Utils.updateStatus(entry1)
				array.extend(Utils.phraseDeCombat(entry1, entry2))
				Utils.updateStatus(entry2)
			else:
				array.append(Utils.phraseDeCombat(entry1, entry2))
				Utils.updateStatus(entry2)
				array.extend(Utils.phraseDeCombat(entry2, entry1))
				Utils.updateStatus(entry1)
			
			turnsCount+=1
		if entry1.availableToFight:
			entry1.increaseCrewLevel()
			array.extend(Utils.phraseDeVictoire(entry1))
		else:
			entry2.increaseCrewLevel()
			array.extend(Utils.phraseDeVictoire(entry2))
		return array


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
		array=[]
		if entryA.isinstance()=="Joueur":
			if entryB.isinstance()=="Joueur":
				array.append(Message("L'équipage de "+entryA.username+" attaque:", True)+entryA.equipage.attaque(entryB.equipage))
			elif entryB.isinstance()=="Equipage":
				array.append(Message("L'équipage de "+entryA.username+" attaque:", True)+entryA.equipage.attaque(entryB))
		elif entryA.isinstance()=="Equipage":
			if entryB.isinstance()=="Joueur":
				array.append(Message("Tour de l'équipage PNJ d'attaquer:")+ entryA.attaque(entryB.equipage))
			elif entryB.isinstance()=="Equipage":
				array.append(Message("Tour de l'équipage PNJ d'attaquer:")+entryA.attaque(entryB))
			
		return array
		

	@staticmethod
	def phraseDeVictoire(entry):
		array=[]
		if entry.isinstance()=="Joueur":
			array.append([Message("L'équipage de "+entry.username+" remporte le combat, ils remportent tous un niveau:", True, "rouge"),Message(str(entry.equipage))])
		elif entry.isinstance()=="Equipage":
			array.append(Message("L'équipage PNJ remporte le combat!", True, "rouge"))
		return array


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






