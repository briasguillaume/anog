import mariadb

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



	@staticmethod
	def getMyCrew(username):
		piratesid=getMyPiratesID(username)

		pirates=[]
		for pirateid in piratesid:
			request = "SELECT * FROM pirate WHERE id='"+pirateid+"';"
		    description = connectAndExecuteRequest(request)
		    txt=""
		    for elem in description:
		    	

		    pirates.append(txt)
	    return pirates



	@staticmethod
	def getMyPiratesID(username):
		request = "SELECT piratesid FROM equipage WHERE username='"+username+"';"
	    description = connectAndExecuteRequest(request)
	    
	    for elem in description:
	    	return str(elem[0]).split(",")
	    		
	    return []



	#____________________________________________________________
	
	@staticmethod
	def connectAndExecuteRequest(request):
	    conn = mariadb.connect(**config)
	    cur = conn.cursor()
	    cur.execute(request)
	    
	    description=cur
	    conn.close
	    return description



