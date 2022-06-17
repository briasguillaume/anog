

class StatsPirate(object):



	@staticmethod
	def generateStats(level, qualite, fruitpower):
		vie=100*level*(5-qualite)
		degats=20*level*(5-qualite)
		defense=10*level*(5-qualite)
		fatigue=100*(5-qualite)
		return [vie+fruitsPower[0], degats+fruitsPower[1], defense+fruitsPower[2], fatigue+fruitsPower[3]]