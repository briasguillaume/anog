
class Stage(object):


	def __init__(self, islands, avancee):
		self._islands=islands
		self._avancee=avancee


	@property
	def islands(self):
		return self._islands


	@property
	def avancee(self):
		return self._avancee



	def __str__(self):
		txt="Les prochaines iles sont: \n"
		count=0
		for island in self._islands:
			txt=txt+"Choix "+str(count)+": "+str(island)
			count+=1

		return txt