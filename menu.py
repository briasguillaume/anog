
from joueur import Joueur
from utils import Utils

class Menu(object):

	debug=False


	def __init__(self):
		self._steps={"1": "Menu.askForUsername",
						"2": "Menu.askForPassword"}
		self._currentStep=1

		self._userInput=[]



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
				txt=Menu.beginningHTML() + eval(self._steps[self._currentStep] + "()") + Menu.endHTML()

			self._userInput.append(user_input)
			self._currentStep+=1
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