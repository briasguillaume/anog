

class StatsPirate(object):



	@staticmethod
	def generateStats(level, qualite, fruitpower):
		vie=100*level*(5-qualite)
		degats=20*level*(5-qualite)
		defense=10*level*(5-qualite)
		fatigue=100*(5-qualite)
		return [vie+fruitpower[0], degats+fruitpower[1], defense+fruitpower[2], fatigue+fruitpower[3]]