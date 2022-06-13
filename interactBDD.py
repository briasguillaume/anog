import mariadb
from pirate import Pirate
from fruitdemon import FruitFactory
from island import Island
from world import World

class Static:
	def __new__(cls):
		raise TypeError('Static classes cannot be instantiated')


class InteractBDD(Static):

	config = {
	    'host': 'mariadb-anog-service',
	    'port': 3306,
	    'user': 'root',
	    'password': 'pwd',
	    'database': 'data'
	}


	#___________________________CREDENTIALS_______________________

	@staticmethod
	def existInDB(username):
	    request = "SELECT username FROM joueur WHERE username='"+username+"';"
	    description = InteractBDD.connectAndExecuteRequest(request, False)
	    
	    for elem in description:
	    	if str(elem[0])==username:
	    		return True
	    return False



	@staticmethod
	def createUser(username, password):
		request = "INSERT INTO joueur VALUES('"+username+"','"+password+"');"
		description = InteractBDD.connectAndExecuteRequest(request, True)
		return None


	@staticmethod
	def checkPassword(username, password):
		request = "SELECT password FROM joueur WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False)

		for elem in description:
			if str(elem[0])==password:
				return True
		return False


	#_________________________GET___________________________

	@staticmethod
	def getMyCrew(username):
		piratesid=InteractBDD.getMyPiratesID(username)

		pirates=[]
		for pirateid in piratesid:
			request = "SELECT * FROM pirate WHERE id='"+pirateid+"';"
			description = InteractBDD.connectAndExecuteRequest(request, False)
			for elem in description:
				level=str(elem[2])
				qualite=str(elem[4])
				fruit=FruitFactory.giveThatFruit(str(elem[3]))
				txt='{"name": '+str(elem[1])+ ', "level": '+level+ ', "qualite": '+qualite+', "fruit": '+ fruit+', "stats": '+str(Pirate.generateStats(level, qualite, fruit.power))+', "availableToFight": True'+', "mort": False}'

				pirates.append(txt) #pas besoin de separation avec une ',', il n'y en a qu'un avec cet id
		return pirates



	@staticmethod
	def getMyPiratesID(username):
		request = "SELECT piratesid FROM equipage WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False)

		for elem in description:
			return str(elem[0]).split(",")

		return []



	@staticmethod
	def getMyLocation(username):
		request = "SELECT position FROM equipage WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False)

		for elem in description:
			name=str(elem[0])
			if name==None:
				return World.carte()[0].islands[0]
			return Island(name, 0,0)
		return World.carte()[0].islands[0]


	#_____________________STORE_______________________________

	@staticmethod
	def setMyCrew(username, position, pirates):

		indexes=""
		for pirate in pirates:
			index=InteractBDD.getAvailableID()
			if not indexes:
				indexes=str(index)
			else:
				indexes=indexes+str(index)
			request = "INSERT INTO pirate VALUES('"+str(index)+"','"+pirate.name+"','"+str(pirate.level)+"','"+pirate.fruit.name+"','"+str(pirate.qualite)+"');"
			description = InteractBDD.connectAndExecuteRequest(request, True)


		request = "DELETE FROM equipage WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, True)


		request = "INSERT INTO equipage VALUES('"+username+"','"+position.name+"','"+indexes+"');"
		description = InteractBDD.connectAndExecuteRequest(request, True)
		return None
	 



	#_________________________DELETE_________________________________


	@staticmethod
	def deleteAll():
		request = "DELETE FROM equipage;"
		description = InteractBDD.connectAndExecuteRequest(request, True)
		request = "DELETE FROM joueur;"
		description = InteractBDD.connectAndExecuteRequest(request, True)
		request = "DELETE FROM pirate;"
		description = InteractBDD.connectAndExecuteRequest(request, True)
		return None


	#____________________________________________________________
	
	@staticmethod
	def connectAndExecuteRequest(request, needCommit):
		conn = mariadb.connect(**InteractBDD.config)
		cur = conn.cursor()
		if needCommit:
			try:
				cur.execute(request)
				conn.commit()
			except:
				conn.rollback()
		else:
			cur.execute(request)

		description=cur
		conn.close
		return description



	@staticmethod
	def getAvailableID():
		index=0
		temp=-1
		request="SELECT id FROM pirate WHERE id="+str(index)+";"
		description = InteractBDD.connectAndExecuteRequest(request, False)
		for elem in description:
			temp=elem[0]
		while temp==index:
			index+=1
			request="SELECT id FROM pirate WHERE id="+str(index)+";"
			description = InteractBDD.connectAndExecuteRequest(request, False)
			for elem in description:
				temp=elem[0]
		return index