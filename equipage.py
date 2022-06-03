
import random
import numpy as np

class Equipage(object):



	def __init__(self, pirates):
		self._team=pirates
		self._turn=np.random.shuffle(np.arange(len(pirates)))
		self._turnCount=0
		self._fatigue=false
		self._mort=false


	@property
	def team(self):
		return self._team

	@property
	def fatigue(self):
		return self._fatigue

	@property
	def mort(self):
		return self._mort

	
	def add(self, pirate):
		self._team.append(pirate)
		self.newFighter()
		self._fatigue=false
		self._mort=false


	def attaque(self):



	def nextTurn(self):
		pirate=self._team[self._turn[self._turnCount]]
		self.increaseTurnCount()
		while !pirate.availableToFight():
			self.removeFighter()
			if len(self._turn)==0:
				self._fatigue=true
				return None
			pirate=self._team[self._turn[self._turnCount]]
			self.increaseTurnCount()
		return pirate

	def increaseTurnCount(self):
		self._turnCount+=1
		if self._turnCount==len(self._turn):
			self._turnCount=0


	def removeFighter(self):
		self._turn.remove(self._turnCount)

	def newFighter(self):
		




class Turn(object):

	def __init__(self, pirate, place):
		self._pirates=pirates
		self._turnCount=0


	def add(self, pirate):


































