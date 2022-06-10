
from joueur import Joueur
from utils import Utils

class Menu(object):

	debug=False
	userInput=["Beefr", "b"]
	steps={1: "Menu.askForUsername", 2: "Menu.askForPassword", 3: "Joueur"}
	parameters={1: [], 2: [], 3: [userInput[0], userInput[1]]}
	currentStep=1



	def __init__(self):
		print("")



	@staticmethod
	def showMenu(user_input):
		if Menu.debug:
			Utils.clear()
			print("Bonjour et bienvenu dans ce petit jeu! ;)\n")
			username = input ("Pouvez-vous indiquer votre nom d'utilisateur?")
			password = input ("Et votre mot de passe?")
			Joueur(username, password)
		else:
			return "" + Menu.getParameters()
			txt=Menu.beginningHTML() + eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")") + Menu.endHTML()

			Menu.nextStep(user_input)
			return txt

	@staticmethod
	def nextStep(user_input):
		if user_input!="":
			if Menu.currentStep<3:
				Menu.currentStep+=1
			if Menu.currentStep==3:
				Menu.userInput=[]
			Menu.userInput.append(user_input)


	@staticmethod
	def getParameters():
		array=Menu.parameters[Menu.currentStep]
		txt=""
		for param in array:
			txt=txt+eval(param)
		return txt


	@staticmethod
	def askForUsername():
		txt="Bonjour et bienvenu dans ce petit jeu! ;) <br>" + "Pouvez-vous indiquer votre nom d'utilisateur? <br>"
		return txt


	@staticmethod
	def askForPassword():
		txt="Et votre mot de passe? <br>" 
		return txt



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