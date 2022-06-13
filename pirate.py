
from abc import abstractmethod
from fruitdemon import FruitFactory
import random
from fruitdemon import FruitDemon


class Pirate(object):

	def __init__(self, level, capitaine=False):
		if capitaine:
			self._qualite=1
			self._fruit=FruitFactory.giveAFruit()
		else:
			self._qualite=self.generateQualite([1,10,50,100])
			self._fruit=FruitFactory.allocateFruit([1,100])

		self._name=self.generateNewName()
		self._level=level
		self._stats=Pirate.generateStats(self._level, self._qualite, self._fruit.power)
		self._availableToFight=True
		self._mort=False


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

	@property
	def qualite(self):
		return self._qualite
		
	@property
	def mort(self):
		if self._stats[0]<=0:
			self._mort=True
		return self._mort

	@fruit.setter
	def fruit(self, frui):
		self._fruit=frui
		self._stats=Pirate.generateStats(self._level, self._qualite, self._fruit.power)

	def regenerateHealth(self):
		self._stats[0]=100*self._level*(5-self._qualite)

	
	def increaseLevel(self):
		self._level+=1
		self._stats=Pirate.generateStats(self._level, self._qualite, self._fruit.power)


	def attaque(self):
		return self._stats[1]


	def fatigue(self):
		return self._stats[3]

	def increaseFatigue(self):
		self._stats[3]-=1
		if self._stats[3]<=0:
			self._availableToFight=False


	def updateStatus(self):
		self._mort=self.mort
		self._availableToFight= self._stats[3]>0
		return self._mort

	def getAttackedBy(self, pirate):
		degats=pirate.attaque()-self._stats[2]
		if degats<=0: #aucun degat reçu
			txt=self._name+" reçoit 0 pts de degats de la part de "+pirate.name+", il garde ses "+str(self._stats[0])+"pts de vie"
			pirate.increaseFatigue()
			return txt
		self._stats[0]=self._stats[0]-degats

		txt=self._name+" reçoit "+str(degats)+"pts de degats de la part de "+pirate.name+", il ne lui reste plus que "+str(self._stats[0])+"pts de vie"
		pirate.increaseFatigue()
		if self._stats[0]<=0:
			self._availableToFight=False
			self._mort=True
		return txt

	def generateNewName(self):
		return Firstname()+Secondname()
		


	def giveAFruit(self, fruit):
		if fruit=="":
			return FruitFactory.giveAFruit()
		else:
			return FruitFactory.giveThatFruit(fruit)

	@staticmethod
	def generateStats(level, qualite, fruitsPower):
		'''
		vie=100*self._level*(5-self._qualite)
		degats=20*self._level*(5-self._qualite)
		defense=10*self._level*(5-self._qualite)
		fatigue=100*(5-self._qualite)

		if self._fruit==None:
			return [vie, degats, defense, fatigue]
		return [vie, degats, defense, fatigue]+self._fruit.power
		'''
		vie=100*level*(5-qualite)
		degats=20*level*(5-qualite)
		defense=10*level*(5-qualite)
		fatigue=100*(5-qualite)
		return [vie, degats, defense, fatigue]+fruitsPower


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


	def __str__(self):
		txt=self._name+"\n"
		txt=txt+"niveau: "+str(self._level)+" | qualité: "+str(self._qualite)+" | fruit: "+self._fruit.name+"\n"
		txt=txt+"vie: "+str(self._stats[0])+" | dps: "+str(self._stats[1])+" | def: "+str(self._stats[2])+" | fatigue: "+str(self._stats[3])+"\n"
		txt=txt+"___________________________________________________\n"
		return txt





class Name(object):


	def __init__(self, name):
		self._name=name


	@abstractmethod
	def generateName(self):
		raise NotImplementedError("Hey, Don't forget to implement")


	@property
	def name(self):
		return self._name




class Firstname(Name):

	def __init__(self):
		firstname=self.generateName()
		super().__init__(firstname)


	def generateName(self):
		dictionnaire=["Kevin", "Roger", "Tiburce", "Gertrude", "Berthe", "Robert", "Blaise", "Titeuf", "Bob", "Berenice", "Benedicte"]
		index=random.randint(0,len(dictionnaire)-1)
		return dictionnaire[index]


	def __add__(self, secondname):
		return self._name+" "+secondname.name






class Secondname(Name):

	def __init__(self):
		secondname=self.generateName()
		super().__init__(secondname)


	def generateName(self):
		dictionnaire=["Tapedur", "Tankfor", "Grossbarb", "Epeenmousse", "Lechauv", "Coursurpat", "Penkibit", "Grofiak", "Moudujnou", "potremalin"]
		index=random.randint(0,len(dictionnaire)-1)
		return dictionnaire[index]






