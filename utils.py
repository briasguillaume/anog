import random
import numpy as np
import os

from fruitdemon import FruitDemon
from fruitdemon import FruitFactory
from multiLineMessage import MultiLineMessage
from pirate import Pirate
from message import Message

import json
from collections import namedtuple
from json import JSONEncoder

import hashlib

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(entry1, entry2):		
		array= MultiLineMessage()
		first=random.randint(1,2)
		turnsCount=0
		while entry1.availableToFight and entry2.availableToFight:
			array+ Message("Tour "+str(turnsCount), True)
			if first==1:
				array+ Utils.phraseDeCombat(entry2, entry1)
				Utils.updateStatus(entry1)
				array+ Utils.phraseDeCombat(entry1, entry2)
				Utils.updateStatus(entry2)
			else:
				array+ Utils.phraseDeCombat(entry1, entry2)
				Utils.updateStatus(entry2)
				array+ Utils.phraseDeCombat(entry2, entry1)
				Utils.updateStatus(entry1)
			
			turnsCount+=1
		if entry1.availableToFight:
			entry1.increaseCrewLevel()
			array+ Utils.phraseDeVictoire(entry1)
		else if entry.isinstance()=="Joueur":
			entry2.increaseCrewLevel()
			array+ Utils.phraseDeVictoire(entry2)
		return array


	@staticmethod
	def increaseCrewLevel(entry):
		if entry.isinstance()=="Joueur":
			entry.equipage.increaseCrewLevel()
		


	@staticmethod
	def updateStatus(entry):
		if entry.isinstance()=="Joueur":
			entry.equipage.updateStatus()
		elif entry.isinstance()=="Equipage":
			entry.updateStatus()


	@staticmethod
	def phraseDeCombat(entryA, entryB):
		if entryA.isinstance()=="Joueur":
			if entryB.isinstance()=="Joueur":
				output = MultiLineMessage()
				output+ Message("L'équipage de "+entryA.username+" attaque:", True)
				output+ entryA.equipage.attaque(entryB.equipage)
				return output
			elif entryB.isinstance()=="Equipage":
				output = MultiLineMessage()
				output+ Message("L'équipage de "+entryA.username+" attaque:", True)
				output+ entryA.equipage.attaque(entryB)
				return output
		elif entryA.isinstance()=="Equipage":
			if entryB.isinstance()=="Joueur":
				output = MultiLineMessage()
				output+ Message("Tour de l'équipage PNJ d'attaquer:")
				output+ entryA.attaque(entryB.equipage)
				return output
			elif entryB.isinstance()=="Equipage":
				output = MultiLineMessage()
				output+ Message("Tour de l'équipage PNJ d'attaquer:")
				output+ entryA.attaque(entryB)
				return output
		
		

	@staticmethod
	def phraseDeVictoire(entry):
		if entry.isinstance()=="Joueur":
			output= MultiLineMessage()
			output+ Message("L'équipage de "+entry.username+" remporte le combat, ils remportent tous un niveau:", True, True, "rouge")
			output+ entry.equipage.asMessageArray()
			return output
		elif entry.isinstance()=="Equipage":
			return Message("L'équipage PNJ remporte le combat!", True, True, "rouge")


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


	@staticmethod
	def hashPassword(password):
		# https://docs.python.org/fr/3/library/hashlib.html
		password=hashlib.blake2b(password.encode('utf-8')).hexdigest()
		try:
			password=password[0:240]
		except:
			pass
		return password
		


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






