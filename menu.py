
from joueur import Joueur
from pirate import Pirate
from interactBDD import InteractBDD

class Menu(object):

	debug=False
	userInput=[]
	steps={ 1: "self.instanciateJoueur",
			2: "self.choseThatIsland", 
			3: "self.choseThatPirate"}
	parameters={1: "[Menu.userInput[0],Menu.userInput[1]]",  
				2: "[Menu.userInput[-1]]",  
				3: "[Menu.userInput[-1]]"}
	currentStep=0
	tempData=None


	def __init__(self):
		self._joueur=None
		Menu.userInput=[]
		Menu.currentStep=0



	@property
	def joueur(self):
		return self._joueur

	@joueur.setter
	def joueur(self, joueur):
		self._joueur=joueur


	def showMenu(self, user_input):
		if Menu.debug:
			print("Bonjour et bienvenu dans ce petit jeu! ;)\n")
			username = input ("Pouvez-vous indiquer votre nom d'utilisateur?")
			password = input ("Et votre mot de passe?")
			Joueur(username, password).showMenu()
		else:
			Menu.nextStep(user_input)
			txt=Menu.beginningHTML() + str(eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")")) + Menu.endHTML()
			
			#txt=txt+"input: "+str(Menu.userInput)
			return txt

	@staticmethod
	def showLogin(addedTxt):
		txt=Menu.beginningHTML()
		txt=txt+addedTxt+"<br>"
		txt=txt+Menu.askForUsername()+Menu.askForPassword()
		txt=txt+"""
			            <form action="/" method="post">
			                Username: <input type="text" name="username" /> <br>
			                Password: <input type="text" name="password" /> <br>
			                <input type="submit" value="Submit" />
			            </form>
			        </p>
			    </body>
			</html>
			"""
		return txt

	@staticmethod
	def nextStep(user_input):
		if user_input!="":
			if Menu.currentStep==0:
				Menu.userInput.append(user_input[0])
				Menu.userInput.append(user_input[1])
			else:
				Menu.userInput.append(user_input)

			if Menu.currentStep<3:
				Menu.currentStep+=1
			elif Menu.currentStep==3:
				Menu.currentStep=2


	@staticmethod
	def getParameters():
		array=eval(Menu.parameters[Menu.currentStep])
		txt=""
		if array!=[]:
			for param in array:
				if txt!="":
					txt=txt+","
				txt=txt+'"'+param+'"'
		return txt


	@staticmethod
	def askForUsername():
		txt="Bonjour et bienvenu dans ce petit jeu! ;) <br>" + "Pouvez-vous indiquer votre nom d'utilisateur? <br>"
		return txt


	@staticmethod
	def askForPassword():
		txt="Et votre mot de passe? <br>" 
		return txt

	
	def choseThatIsland(self, value):
		txt=self._joueur.goingToNextIsland(value)
		txt=txt+Menu.askForRecruitment(self._joueur)
		return txt


	def choseThatPirate(self, value):
		if self._joueur.availableToFight():
			return self._joueur.recrutement(len(Menu.tempData), Menu.tempData, value)
		else:
			InteractBDD.deleteUserProgress(self._username)
			InteractBDD.setMyCrew(self._username, World.carte()[0].islands[0].name, [Pirate(1, True)])
			return "Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n <br>"
			

		

	@staticmethod
	def askForRecruitment(joueur):
		pirates=[]
		number=5
		txt="Des pirates sont disponibles au recrutement. <br>"
		for i in range(0,number):
			pirate=Pirate(joueur.position.level)
			pirates.append(pirate)
			txt=txt+"Choix "+str(i)+": "+str(pirate)

		txt=txt+"Lequel voulez-vous recruter?<br>"
		Menu.tempData=pirates
		return txt

	
	def instanciateJoueur(self, username, password):
		self._joueur=Joueur(username, password)
		if self._joueur.username==None: #wrong password
			self._joueur=None
			Menu.userInput=[]
			Menu.currentStep=0
			return Menu.showLogin("Wrong password, try again.")
		return self._joueur.showMenu()

	@staticmethod
	def beginningHTML():
		return """
			<!DOCTYPE html>
			<html>
			    <head>
			        <title>
			            ANOG
			        </title>
			    </head>
			    <body>
			        <h3>
			            ANOG: Another Neat Onepiece Game - by Corentin RENAULT & Adrien TURCHET
			        </h3>
			        <p>
			            """


	@staticmethod
	def endHTML():
		return """
			            <form action="/" method="post">
			                User input: <input type="text" name="user_input" />
			                <input type="submit" value="Submit" />
			            </form>
			        </p>
			    </body>
			</html>
			"""



	@staticmethod
	def clean():
		return InteractBDD.deleteAll()