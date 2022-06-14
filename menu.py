
from joueur import Joueur

class Menu(object):

	debug=False
	userInput=[]
	steps={	1: "Menu.askForUsername", 
			2: "Menu.askForPassword", 
			3: "self.instanciateJoueur", 
			#4: "Menu.askForNextIsland", 
			4: "self.choseThatIsland", 
			5: "Menu.askForRecruitment", 
			6: "self.choseThatPirate"}
	parameters={1: "[]", 
				2: "[]", 
				3: "[Menu.userInput[0], Menu.userInput[1]]", 
				#4: "[]", 
				4: "[Menu.userInput[-1]]", 
				5: "[]", 
				6: "[Menu.userInput[-1]]"}
	currentStep=1
	tempData=None


	def __init__(self):
		self._joueur=None
		


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
			txt=Menu.beginningHTML() + str(eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")")) + Menu.endHTML()

			if Menu.currentStep==2:
				Menu.userInput=[Menu.userInput[-1]]

			Menu.nextStep(user_input)
			return txt

	@staticmethod
	def nextStep(user_input):
		if user_input!="":
			if Menu.currentStep==3:
				Menu.userInput=[]
			if Menu.currentStep<6:
				Menu.currentStep+=1
			elif Menu.currentStep==6:
				Menu.currentStep=4
			Menu.userInput.append(user_input)


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
		self._joueur.goingToNextIsland(value)


	def choseThatPirate(self, value):
		self._joueur.recrutement(len(Menu.tempData), Menu.tempData, value)

	@staticmethod
	def askForRecruitment(joueur):
		pirates=[]
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
		return InteractBDD.clean()