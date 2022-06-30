
class Stage(object):

	def __init__(self, islands):
		self._islands=islands


	@property
	def islands(self):
		return self._islands


	def __str__(self):
		txt="Les prochaines iles sont:\n"
		count=0
		for island in self._islands:
			txt=txt+"Choix "+str(count)+": "+str(island)+"\n"
			count+=1
		txt=txt+"\n"
		return txt