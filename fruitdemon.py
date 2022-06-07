
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
		print("hello")



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
	def giveAFruit():
		if True:
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


























