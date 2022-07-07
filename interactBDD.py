import mariadb

from fruitdemon import FruitFactory
from statsPirate import StatsPirate


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
		[conn, cur]=InteractBDD.beginQuery()
		request = "SELECT username FROM joueur WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		
		for elem in description:
			if str(elem[0])==username:
				InteractBDD.endQuery(conn, cur)
				return True
		InteractBDD.endQuery(conn, cur)
		return False


	@staticmethod
	def createUser(username, password):
		[conn, cur]=InteractBDD.beginQuery()
		request = "INSERT INTO joueur VALUES('"+username+"','"+password+"');"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		InteractBDD.endQuery(conn, cur)
		return None


	@staticmethod
	def checkPassword(username, password):
		[conn, cur]=InteractBDD.beginQuery()
		request = "SELECT password FROM joueur WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)

		for elem in description:
			if str(elem[0])==password:
				InteractBDD.endQuery(conn, cur)
				return True
		InteractBDD.endQuery(conn, cur)
		return False


	#_________________________GET___________________________

	@staticmethod
	def getMyCrew(username):
		[conn, cur]=InteractBDD.beginQuery()
		pirates=[]
		request = "SELECT * FROM pirate WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			level=elem[2]
			qualite=elem[4]
			fruit=FruitFactory.giveThatFruit(str(elem[3]))
			txt='{"type": "Pirate", "name": \"'+str(elem[1])+'\", "level": '+str(level)+ ', "qualite": '+str(qualite)+', "fruit": '+ str(fruit)+', "stats": '+str(StatsPirate.generateStats(level, qualite, fruit.power))+', "availableToFight": "True", "mort": "False"}'
			pirates.append(txt) #pas besoin de separation avec une ',', il n'y en a qu'un avec cet id
		InteractBDD.endQuery(conn, cur)
		return pirates


	@staticmethod
	def getMyLocation(username):
		[conn, cur]=InteractBDD.beginQuery()
		request = "SELECT position FROM island WHERE username='"+username+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			value = str(elem[0])
			InteractBDD.endQuery(conn, cur)
			return value
		return ""
		
	@staticmethod
	def retrieveWholeDatabase():
		[conn, cur]=InteractBDD.beginQuery()
		txt=""

		txt=txt+"Joueur: <br>"
		txt=txt+"username | password <br>"
		request = "select * from joueur;"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			for i in range(len(elem)):
				txt= txt+"| " + str(elem[i])
			txt=txt+"<br>"
		txt=txt+"<br>"

		txt=txt+"Position: <br>"
		txt=txt+"username | position's name <br>"
		request = "select * from island;"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			for i in range(len(elem)):
				txt= txt+"| " + str(elem[i])
			txt=txt+"<br>"
		txt=txt+"<br>"

		txt=txt+"Pirate: <br>"
		txt=txt+"owner | name | level | fruit's name | qualite <br>"
		request = "select * from pirate;"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			for i in range(len(elem)):
				txt= txt+" | " + str(elem[i])
			txt=txt+"<br>"
		txt=txt+"<br>"

		InteractBDD.endQuery(conn, cur)
		return txt
		# TODO maybe add an input to execute requests?
		# TODO add a security before that route and... the other one...


	@staticmethod
	def checkPlayer(islandName):
		[conn, cur]=InteractBDD.beginQuery()
		request = "SELECT username FROM island WHERE position='"+islandName+"';"
		description = InteractBDD.connectAndExecuteRequest(request, False, conn, cur)
		for elem in description:
			value = str(elem[0])
			InteractBDD.endQuery(conn, cur)
			return value
		InteractBDD.endQuery(conn, cur)
		return None


	#_____________________STORE_______________________________

	@staticmethod
	def setMyCrew(username, positionsName, pirates):
		[conn, cur]=InteractBDD.beginQuery()

		for pirate in pirates:
			request = "INSERT INTO pirate VALUES('"+username+"','"+pirate.name+"','"+str(pirate.level)+"','"+pirate.fruit.name+"','"+str(pirate.qualite)+"');"
			InteractBDD.connectAndExecuteRequest(request, True, conn, cur)

		request = "UPDATE island SET position='"+positionsName+"' WHERE username='"+username+"';"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)

		InteractBDD.endQuery(conn, cur)
		return None
	
	@staticmethod
	def setMyLocation(username, positionsName):
		[conn, cur]=InteractBDD.beginQuery()
		request = "UPDATE island SET position='"+positionsName+"' WHERE username='"+username+"';"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		InteractBDD.endQuery(conn, cur)
		return None

	@staticmethod
	def addNewFighter(username, pirate):
		[conn, cur]=InteractBDD.beginQuery()
		request = "INSERT INTO pirate VALUES('"+username+"','"+pirate.name+"','"+str(pirate.level)+"','"+pirate.fruit.name+"','"+str(pirate.qualite)+"');"
		description = InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		InteractBDD.endQuery(conn, cur)
		return None


	@staticmethod
	def increasePirateLevel(username):
		[conn, cur]=InteractBDD.beginQuery()

		request = "UPDATE pirate SET level=level+1 WHERE username='"+username+"' and fruit=\"None\";"
		description = InteractBDD.connectAndExecuteRequest(request, True, conn, cur)

		request = "UPDATE pirate SET level=level+3 WHERE username='"+username+"' and fruit!=\"None\";"
		description = InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		InteractBDD.endQuery(conn, cur)
		return None


	#_________________________DELETE_________________________________


	@staticmethod
	def deleteUserProgress(username):

		[conn, cur]=InteractBDD.beginQuery()

		request = "DELETE FROM island WHERE username='"+username+"';"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)

		request = "DELETE FROM pirate WHERE username='"+username+"';"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur) # TODO remove allocated fruits

		InteractBDD.endQuery(conn, cur)
		return None


	@staticmethod
	def deleteAll():
		[conn, cur]=InteractBDD.beginQuery()
		request = "DELETE FROM island;"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		request = "DELETE FROM joueur;"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		request = "DELETE FROM pirate;"
		InteractBDD.connectAndExecuteRequest(request, True, conn, cur)
		InteractBDD.endQuery(conn, cur)
		return None


	@staticmethod
	def removeFighter(username, pirate):
		[conn, cur]=InteractBDD.beginQuery()

		request = "DELETE FROM pirate WHERE username='"+username+"' and name='"+pirate.name+"' and fruit='"+pirate.fruit.name+"' and level='"+str(pirate.level)+"' and qualite='"+str(pirate.qualite)+"';"
		description = InteractBDD.connectAndExecuteRequest(request, True, conn, cur)

		InteractBDD.endQuery(conn, cur)
		return None


	#____________________________________________________________
	
	@staticmethod
	def connectAndExecuteRequest(request, needCommit, conn, cur):
		#conn = mariadb.connect(**InteractBDD.config)
		#cur = conn.cursor()
		if needCommit:
			try:
				cur.execute(request)
				conn.commit()
			except:
				conn.rollback()
		else:
			cur.execute(request)

		description=cur
		#cur.close()
		#conn.close()
		return description

	@staticmethod
	def beginQuery():
		conn = mariadb.connect(**InteractBDD.config)
		cur = conn.cursor()
		return [conn, cur]

	@staticmethod
	def endQuery(conn, cur):
		cur.close()
		conn.close()
		
