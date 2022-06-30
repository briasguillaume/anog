
class Stage(object):

	def __init__(self, islands):#, avancee):
		self._islands=islands
		#self._avancee=avancee


	@property
	def islands(self):
		return self._islands


	def __str__(self):
		txt="<br>Les prochaines iles sont: <br>"
		count=0
		for island in self._islands:
			txt=txt+"Choix "+str(count)+": "+str(island)+"<br>"
			count+=1
		txt=txt+"<br>"
		return txt