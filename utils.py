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

	debug=False

	@staticmethod
	def fight(entry1, entry2):

		if Utils.debug:
			if entry1.isinstance()=="Joueur":
				equipage1=entry1.equipage
			elif entry1.isinstance()=="Equipage":
				equipage1=entry1 

			if entry2.isinstance()=="Joueur":
				equipage2=entry2.equipage
			elif entry2.isinstance()=="Equipage":
				equipage2=entry2 
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
			txt="<p>"
			first=random.randint(1,2)
			turnsCount=0
			while entry1.availableToFight and entry2.availableToFight:
				txt=txt+"<b>Tour "+str(turnsCount)+":</b><br>"
				txt=txt+Utils.phraseDeCombat(entry2, entry1)
				Utils.updateStatus(entry1)
				txt=txt+Utils.phraseDeCombat(entry1, entry2)
				Utils.updateStatus(entry2)
				txt=txt+"<br>"
				turnsCount+=1
			if entry1.availableToFight:
				entry1.increaseCrewLevel()
				# TODO interactBDD.increaseCrewLevel(joueur1.username)
				txt=txt+Utils.phraseDeVictoire(entry1)
			else:
				entry2.increaseCrewLevel()
				txt=txt+Utils.phraseDeVictoire(entry2)
			return txt+"</p>"


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
		txt="<p>"
		if entryA.isinstance()=="Joueur":
			if entryB.isinstance()=="Joueur":
				txt=txt+"L'équipage de <b>"+entryA.username+"</b> attaque:"+entryA.equipage.attaque(entryB.equipage)+"<br>"
			elif entryB.isinstance()=="Equipage":
				txt=txt+"L'équipage de "+entryA.username+" attaque:"+entryA.equipage.attaque(entryB)+"<br>"
		elif entryA.isinstance()=="Equipage":
			if entryB.isinstance()=="Joueur":
				txt=txt+"Tour de l'équipage PNJ d'attaquer:"+entryA.attaque(entryB.equipage)+"<br>"
			elif entryB.isinstance()=="Equipage":
				txt=txt+"Tour de l'équipage PNJ d'attaquer:"+entryA.attaque(entryB)+"<br>"
			
		return txt +"</p>"
		

	@staticmethod
	def phraseDeVictoire(entry):
		txt="<p>"
		if entry.isinstance()=="Joueur":
			txt=txt+"L'équipage de <b>"+entry.username+"</b> remporte le combat, ils remportent tous un niveau:<br>"+str(entry.equipage)+"<br>"
		elif entry.isinstance()=="Equipage":
			txt=txt+"L'équipage PNJ remporte le combat! <br>"#, ils remportent tous un niveau:<br>"+str(entry)+"<br>"
		return txt+"</p>"


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






