
import random

class FruitDemon(object):

	def __init__(self, name, power):
		self._name=name
		self._power=power


	@property
	def power(self):
		return self._power


	@property
	def name(self):
		return self._name



	@power.setter
	def power(self, power):
		self._power=power


	@name.setter
	def name(self, name):
		self._name=name

	def __str__(self):
		return '{"type": "FruitDemon", "name": \"'+self._name+'\","power": '+str(self._power)+'}'
	

class FruitFactoryMeta(type):

	_instances = {}

	def __call__(cls, *args, **kwargs):
		"""
		Possible changes to the value of the `__init__` argument do not affect
		the returned instance.
		"""
		if cls not in cls._instances:
			instance = super().__call__(*args, **kwargs)
			cls._instances[cls] = instance
		return cls._instances[cls]



class FruitFactory(metaclass=FruitFactoryMeta):

	fruitsNames=["GumGum", "Fire", "Ice", "Electric"]
	fruitsPower={"GumGum":[250,250,250,250], 
				"Fire":[250,500,0,250], 
				"Ice":[250,300,500,250], 
				"Electric":[500,0,0,500]}
	allocatedFruits={"GumGum":False, 
				"Fire":False, 
				"Ice":False, 
				"Electric":False}
	#todo: create a database to avoid class variables


	def countAvailableFruits():
		count=0
		for fruit in FruitFactory.fruitsNames:
			if FruitFactory.allocatedFruits[fruit]==False:
				count=count+1
		return count


	@staticmethod
	def allocateFruit(percentages):
		fruitBool=random.randint(0,100)<=percentages[0]
		if fruitBool:
			availableFruits=FruitFactory.countAvailableFruits()
			if availableFruits==0:
				return FruitDemon("None",[0,0,0,0])

			fruitsNumber=random.randint(0,availableFruits-1)
			count=0
			for fruit in FruitFactory.fruitsNames:
				if FruitFactory.allocatedFruits[fruit]==False:
					if count==fruitsNumber:
						FruitFactory.allocatedFruits[fruit]=True
						return FruitDemon(fruit,FruitFactory.fruitsPower[fruit])
					count+=1

			
		return FruitDemon("None",[0,0,0,0])


	@staticmethod
	def giveThatFruit(fruit):
		if fruit=="None":
			return FruitDemon("None",[0,0,0,0])

		return FruitDemon(fruit, FruitFactory.fruitsPower[fruit])

	@staticmethod
	def giveAFruit():
		#availableFruits=FruitFactory.countAvailableFruits()
		availableFruits=len(FruitFactory.fruitsNames)
		#if availableFruits==0:
		#	return FruitDemon("None",[0,0,0,0])
		# TODO it is bugged
		fruitsNumber=random.randint(0,availableFruits-1)
		count=0
		for fruit in FruitFactory.fruitsNames:
			if FruitFactory.allocatedFruits[fruit]==False:
				if count==fruitsNumber:
					#FruitFactory.allocatedFruits[fruit]=True
					return FruitDemon(fruit,FruitFactory.fruitsPower[fruit])
				count+=1

			
		#return FruitDemon("None",[0,0,0,0])
		return FruitFactory.giveThatFruit("GumGum")


























