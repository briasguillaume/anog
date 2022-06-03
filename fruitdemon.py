
import random

class FruitDemon(object):
	fruitsNames=["GumGum", "Fire", "Ice", "Electric"]
	fruitsPower={"GumGum":[25,25,25,25], 
				"Fire":[25,50,0,25], 
				"Ice":[25,0,50,25], 
				"Electric":[50,0,0,50]}
	allocatedFruits={"GumGum":False, 
				"Fire":False, 
				"Ice":False, 
				"Electric":False}
	#todo: create a database to avoid class variables

	def __init__(self):
		self._name=self.allocateFruit()
		self._power=fruitsPower[self._name]


	def countAvailableFruits(self):
		count=0
		for fruit in fruitsNames:
			if allocatedFruits[fruit]==False:
				count=count+1
		return count


	def allocateFruit(self):
		availableFruits=self.countAvailableFruits()


		fruitsNumber=random.randint(0,availableFruits-1)
		count=0
		for fruit in fruitsNames:
			if count==fruitsNumber:
				return fruit
			count+=1

		return name


	@property
	def power(self):
		return self._power


	@property
	def name(self):
		return self._name
	