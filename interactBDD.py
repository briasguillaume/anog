import mariadb
from pirate import Pirate
from fruitdemon import FruitFactory

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
	    description = connectAndExecuteRequest(request)
	    
	    for elem in description:
	    	if str(elem[0])==username:
	    		return True
	    return False



	@staticmethod
	def createUser(username, password):
		request = "INSERT INTO joueur VALUES('"+username+"','"+password+"');"
		description = connectAndExecuteRequest(request)



	@staticmethod
	def checkPassword(username, password):
		request = "SELECT password FROM joueur WHERE username='"+username+"';"
	    description = connectAndExecuteRequest(request)
	    
	    for elem in description:
	    	if str(elem[0])==password:
	    		return True
	    return False


	#_________________________GET___________________________

	@staticmethod
	def getMyCrew(username):
		piratesid=getMyPiratesID(username)

		pirates=[]
		for pirateid in piratesid:
			request = "SELECT * FROM pirate WHERE id='"+pirateid+"';"
		    description = connectAndExecuteRequest(request)
		    for elem in description:
		    	level=str(elem[2])
		    	qualite=str(elem[4])
		    	fruit=FruitFactory.giveThatFruit(str(elem[3]))
		    	txt='{"name": '+str(elem[1])+
		    		', "level": '+level+
		    		', "qualite": '+qualite+
		    		', "fruit": '+ fruit+
		    		', "stats": '+str(Pirate.generateStats(level, qualite, fruit.power))+
		    		', "availableToFight": True'+
		    		', "mort": False}'
		    	

		    	pirates.append(txt) #pas besoin de separation avec une ',', il n'y en a qu'un avec cet id
	    return pirates



	@staticmethod
	def getMyPiratesID(username):
		request = "SELECT piratesid FROM equipage WHERE username='"+username+"';"
	    description = connectAndExecuteRequest(request)
	    
	    for elem in description:
	    	return str(elem[0]).split(",")
	    		
	    return []



	@staticmethod
	def getMyLocation(username):
		request = "SELECT position FROM equipage WHERE username='"+username+"';"
	    description = connectAndExecuteRequest(request)
	    
	    for elem in description:
	    	return Island(str(elem[0]), 0,0)


	#_____________________STORE_______________________________

	@staticmethod
	def setMyCrew(username, position, pirates):
		piratesid=""
		for i in range(0,len(pirates)):
			if i==0:
				piratesid=piratesid+pirates[i].name
			else:
				piratesid=piratesid+","+pirates[i].name

		request = "DELETE FROM equipage WHERE username='"+username+"';"
	    description = connectAndExecuteRequest(request)
		request = "INSERT INTO equipage VALUES('"+username+"','"+position+"','"+piratesid+"');"
	    description = connectAndExecuteRequest(request)
	    


	#____________________________________________________________
	
	@staticmethod
	def connectAndExecuteRequest(request):
	    conn = mariadb.connect(**config)
	    cur = conn.cursor()
	    cur.execute(request)
	    
	    description=cur
	    conn.close
	    return description



