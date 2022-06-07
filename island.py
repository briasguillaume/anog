
from equipage import Equipage
from pirate import Pirate




class Island(object):


	def __init__(self, name, level, ennemies):
		self._name=name
		self._level=level
		self._ennemies=ennemies
		self._pirates=Equipage(self.generateEnnemies(level, ennemies))



	def generateEnnemies(self, level, ennemies):
		pirates=[]
		for i in range(ennemies):
			pirates.append(Pirate(level))
		return pirates


	def __str__(self):
		return self._name+", il y a "+str(self._pirates.numberOfPirates)+" pirates de niveau "+str(self._level)+".\n"



	@property
	def name(self):
		return self._name



	@property
	def level(self):
		return self._level



	@property
	def pirates(self):
		return self._pirates


	def regenerate(self):
		self._pirates=Equipage(self.generateEnnemies(self._level, self._ennemies))