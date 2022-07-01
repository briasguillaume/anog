from message import Message

class Stage(object):

	def __init__(self, islands):
		self._islands=islands


	@property
	def islands(self):
		return self._islands


	def __str__(self):
		array=[Message("Les prochaines iles sont:")]
		count=0
		for island in self._islands:
			array.append(Message("Choix "+str(count)+": "+str(island)))
			count+=1
		
		return array