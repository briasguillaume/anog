import random

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class Utils(Static):

	@staticmethod
	def fight(pirates1, pirates2):
		piratesTurn = np.random.shuffle(np.arange(len(pirates1)+len(pirates2)))
		while len(piratesTurn)>0:
			for turn in piratesTurn:

				if turn>=len(pirates1):
					pirate=pirates2[turn-len(pirates1)]
					cible=pirates1[random.randint(0,len(pirates1)-1)]
					while cible.mort():
						pirates1.remove(cible)
						cible=pirates1[random.randint(0,len(pirates1)-1)]
				else:
					pirate=pirates1[turn]
					cible=pirates2[random.randint(0,len(pirates2)-1)]
					while cible.mort():
						pirates2.remove(cible)
						cible=pirates2[random.randint(0,len(pirates2)-1)]
			
				if pirate.fatigue()>0 && !pirate.mort():
					cible.getAttackedBy(pirate)
				else:
					piratesTurn.remove(turn)


					







