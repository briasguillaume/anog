
import random
import numpy as np

class Equipage(object):



	def __init__(self, pirates):
		self._team=pirates
		print(pirates)
		self._turn=Turn(pirates)
		self._availableToFight=True
		self._numberOfPirates=len(self._team)

	@property
	def team(self):
		return self._team

	@property
	def availableToFight(self):
		return self._availableToFight

	@property
	def numberOfPirates(self):
		return self._numberOfPirates


	def attaque(self, equipage):
		pirate=self._turn.next()
		return equipage.whoIsGonnaTankThatHit().getAttackedBy(pirate)

	def whoIsGonnaTankThatHit(self):
		who=random.randint(0, self._numberOfPirates-1)
		return self._team[who]
	



	def removeFighter(self):
		self._turn.removeCurrent()

	def newFighter(self, pirate):
		self._team.append(pirate)
		self._turn.add(pirate)



class Turn(object):

	def __init__(self, pirates):
		self._pirates=np.random.shuffle(pirates)
		self._turnCount=0
		self._numberOfPirates=len(self._pirates)


	def add(self, pirate):
		self._numberOfPirates+=1
		place=random.randint(0,self._numberOfPirates)
		if place==0:
			self._pirates=[pirate, self._pirates]
		elif place==self._numberOfPirates:
			self._pirates.append(pirate)
		else:
			self._pirates=[self._pirates[0:place],pirate, self._pirates[place+1:end]]

	def removeCurrent(self):
		self._numberOfPirates-=1
		self._pirates=np.delete(self._pirates, self._turnCount)

	def next(self):
		if len(self._pirates)==0:
			return None
		self._turnCount+=1
		pirate = self._pirates[self._turnCount]
		if pirate.availableToFight==False:
			self.removeCurrent()
			self.next()

		return pirate



	def __str__(self):
		txt=""
		for pirate in self._team:
			txt=txt+ str(pirate)
		return txt
































