
from abc import abstractmethod
from fruitdemon import FruitDemon
import random
from equipage import Equipage
from fruitdemon import FruitDemon

class Pirate(object):

	def __init__(self, level):
		self._name=self.generateNewName()
		self._level=level
		self._qualite=self.generateQualite([1,10,50,100])
		self._fruit=self.generateFruit(self.generateDemonBool([1,100]))
		self._stats=self.generateStats()
		self._availableToFight=True


	@property
	def name(self):
		return self._name

	@property
	def stats(self):
		return self._stats

	@property
	def availableToFight(self):
		return self._availableToFight

	@property
	def fruit(self):
		return self._fruit

	@property
	def level(self):
		return self._level

	@fruit.setter
	def fruit(self, frui):
		self._fruit=frui
		self._stats=self.generateStats()

	@level.setter
	def level(self):
		self._level+=1
		self._stats=self.generateStats()


	def attaque(self):
		return self._stats[1]


	def fatigue(self):
		return self._stats[3]

	def increaseFatigue(self):
		self._stats[3]-=1
		if self._stats[3]<=0:
			self._availableToFight=False

	def mort(self):
		if self._stats[0]<=0:
			return true
		return false


	def getAttackedBy(self, pirate):
		degats=pirate.attaque()-self._stats[2]
		self._stats[0]=self._stats[0]-degats

		txt=self._name+" receives "+degats+"pts de degats de la part de "+pirate.name()+", il ne lui reste plus que "+self._stats[0]+"pts de vie"
		pirate.increaseFatigue()
		if self._stats[0]<=0:
			self._availableToFight=false
		return txt

	def generateNewName(self):
		return "Toto"



	def generateStats(self):

		vie=100*self._level*self._qualite
		degats=20*self._level*self._qualite
		defense=10*self._level*self._qualite
		fatigue=100*self._qualite

		if self._fruit==None:
			return [vie, degats, defense, fatigue]
		return [vie, degats, defense, fatigue]+self._fruit.power


	def generateQualite(self, percentageQualite):
		percent = random.randint(0,100)
		if percent<=percentageQualite[0]:
			qualite=1
		elif percent<=percentageQualite[1]:
			qualite=2
		elif percent<=percentageQualite[2]:
			qualite=3
		else:
			qualite=4

		return qualite


	def generateDemonBool(self, percentageDemonBool):
		percent = random.randint(0,100)	
		if percent<=percentageDemonBool[0]:
			demonBool=True
		else:
			demonBool=False

		return demonBool

	def generateFruit(self, demonBool):
		if demonBool:
			return FruitDemon()
		return None


	def __str__(self):
		return "Je suis "+self._name+",je suis de niveau "+self._level+" avec une qualité de "+self._qualite+", et je suis le détenteur du fruit du"+self._fruit.name()+"\n"