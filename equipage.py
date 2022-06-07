
import random
import numpy as np
from utils import Utils
from pirate import Pirate

class Equipage(object):



	def __init__(self, pirates):
		self._team=pirates
		self._turn=Turn(pirates)
		self._availableToFight=True
		self._numberOfPirates=len(self._team)

	@property
	def team(self):
		return self._team

	@property
	def availableToFight(self):
		self.isStillAvailableToFight()
		return self._availableToFight

	@property
	def numberOfPirates(self):
		return self._numberOfPirates


	def attaque(self, equipage):
		pirate=self._turn.next()
		return equipage.whoIsGonnaTankThatHit().getAttackedBy(pirate)

	def whoIsGonnaTankThatHit(self):
		alive=self.isStillAvailableToFight()
		who=random.randint(0, self._numberOfPirates-1)
		return alive[who]
	
	def isStillAvailableToFight(self):
		alive=[]
		for pirate in self._team:
			if pirate.mort()==False:
				alive.append(pirate)
		self._numberOfPirates=len(alive)
		if self._numberOfPirates==0:
			self._availableToFight=False
		return alive

	def increaseCrewLevel(self):
		for pirate in self._team:
			pirate.level


	def removeFighter(self):
		self._turn.removeCurrent()

	def newFighter(self, pirate):
		self._team.append(pirate)
		self._turn.add(pirate)

	def __str__(self):
		txt=""
		for pirate in self._team:
			txt=txt+ str(pirate)
		return txt

class Turn(object):

	def __init__(self, pirates):
		self._pirates=Utils.shuffle(pirates)
		self._turnCount=0
		self._numberOfPirates=len(self._pirates)


	def add(self, pirate):
		self._numberOfPirates+=1
		place=random.randint(0,self._numberOfPirates)
		if place==0:
			temp=[pirate]

			for p in self._pirates:
				temp.append(p)

			self._pirates=temp
		elif place==self._numberOfPirates:
			self._pirates.append(pirate)
		else:
			temp=[]
			for p in self._pirates[0:place]:
				temp.append(p)
			
			temp.append(pirate)
			
			for p in self._pirates[place+1:len(self._pirates)-1]:
				temp.append(p)

			self._pirates=temp

	def removeCurrent(self):
		self._numberOfPirates-=1
		self._pirates=np.delete(self._pirates, self._turnCount)

	def next(self):
		if len(self._pirates)==0:
			return None
		self.increaseTurnCount()
		pirate = self._pirates[self._turnCount]
		if pirate.availableToFight==False:
			self.removeCurrent()
			self.next() #recursif jusqu'à trouver un pirate disponible

		return pirate

	def increaseTurnCount(self):
		self._turnCount+=1
		if self._turnCount>=len(self._pirates):
			self._turnCount=0


































