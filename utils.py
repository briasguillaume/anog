import random

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(equipage1, equipage2):
		first=random.randint(1,2)
		while equipage1.availableToFight() and equipage2.availableToFight():
			print(equipage2.attaque(equipage1))
			print(equipage1.attaque(equipage2))



					







