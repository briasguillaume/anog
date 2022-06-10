
from joueur import Joueur
from utils import Utils

class Menu(object):

	debug=False
	steps={"1": "Menu.askForUsername",
						"2": "Menu.askForPassword"}
	currentStep=1

	userInput=[]


	def __init__(self):
		print("")



	@staticmethod
	def showMenu(user_input):
		if Menu.debug:
			Utils.clear()
			print("Bonjour et bienvenu dans ce petit jeu! ;)\n")
			username = input ("Pouvez-vous indiquer votre nom d'utilisateur?")
			password = input ("Et votre mot de passe?")
			Joueur([username, password])
		else:

			while user_input=="": 
				txt=Menu.beginningHTML() + Menu.endHTML()
#+ eval(Menu.steps[Menu.currentStep] + "()") 
			Menu.userInput.append(user_input)
			Menu.currentStep+=1
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