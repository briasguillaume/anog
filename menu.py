
from joueur import Joueur
from interactBDD import InteractBDD
import hashlib
from flask import url_for


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

	#TODO use fruit's allocation
	#TODO hook values from bdd and not code


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
			output=self.checkUserInput(user_input)

			
			return "Connected as: "+self._joueur.username+"<br>"+output

	@staticmethod
	def showLoginOld(addedTxt):
		Menu.userInput=[]
		Menu.currentStep=0
		txt=Menu.beginningHTML()
		txt=txt+addedTxt+"<br>"
		txt=txt+Menu.askForUsername()
		txt=txt+"""
			            <form action="/" method="post" autocomplete="off">
							<div class="form-field">
								Username: <input type="text" placeholder="Username" name="username" required/> <br>
							</div>
							<div class="form-field">
								Password: <input type="password" placeholder="Password" name="password" required/> <br>
							</div>
							<div class="form-field">
								<input type="submit" value="Valider" />
							</div>
							
			            </form>
			            <br><i>- Max 15 characters <br> - No special characters</i>
			        </p>
			    </body>
			</html>
			"""
		return txt



	@staticmethod
	def getParameters():
		array=eval(Menu.parameters[Menu.currentStep])
		txt=""
		if array!=[]:
			for param in array:
				if txt!="":
					txt=txt+","
				try:
					txt=txt+'"'+param+'"'
				except: 
					txt= "Error: list and str concatenation"+str(param)
		return txt


	@staticmethod
	def askForUsername():
		txt="Bonjour et bienvenu dans ce petit jeu! ;) <br>" + "Pouvez-vous indiquer votre nom d'utilisateur? <br>"
		txt=txt+"Et votre mot de passe? <br>"
		return txt


	@staticmethod
	def showLogin(addedText):
		return """
					<!DOCTYPE html>
					<html lang="fr" >
						<head>
							<meta charset="UTF-8">
							<title>
								ANOG
							</title>
							<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css')}}">
						</head>
						<body>
							<div id="bg"></div>
							<h3>
								ANOG: Another Neat Onepiece Game - by Corentin RENAULT & Adrien TURCHET
							</h3>
							<p>
								<div>
									Bonjour et bienvenu dans ce petit jeu! ;) <br>
									Pouvez-vous indiquer votre nom d'utilisateur/mot de passe? <br>
								</div>

								<form action="/" method="post" autocomplete="off">
									<div class="form-field">
										<input type="text" placeholder="Username" name="username" required/> <br>
									</div>
									<div class="form-field">
										<input type="password" placeholder="Password" name="password" required/> <br>
									</div>
									<div class="form-field">
										<button class="btn" type="submit">Valider</button>
									</div>
									
								</form>
								<br><i>- Max 15 characters <br> - No special characters</i>
							</p>
						</body>
					</html>
		
		"""
	
	def choseThatIsland(self, value):
		txt=self._joueur.goingToNextIsland(value)
		txt=txt+self.checkAliveForRecruitment()
		return Menu.beginningHTML() + txt  + Menu.endHTML()


	def choseThatPirate(self, value):
		txt=self._joueur.recrutement(len(Menu.tempData), Menu.tempData, value)
		return Menu.beginningHTML() + txt  + Menu.endHTML()


	def checkAliveForRecruitment(self):
		if self._joueur.availableToFight:
			return self.askForRecruitment()
		else:
			self._joueur.resetCrew()
			txt="Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n <br>"
			return txt

		
	@staticmethod
	def showBDD():
		return Menu.beginningHTML() + InteractBDD.retrieveWholeDatabase() + Menu.endHTML()

	def askForRecruitment(self):
		[txt, Menu.tempData]=self._joueur.askForRecruitment()
		return txt

	
	def instanciateJoueur(self, username, password):
		# https://docs.python.org/fr/3/library/hashlib.html
		password=hashlib.blake2b(password.encode('utf-8')).hexdigest()
		try:
			password=password[0:240]
		except:
			pass
		self._joueur=Joueur(username, password)
		if self._joueur.username==None: #wrong password
			self._joueur=None
			Menu.userInput=[]
			Menu.currentStep=0
			return Menu.showLogin("Wrong password, try again.")
		txt = self._joueur.showMenu()
		return Menu.beginningHTML() + txt  + Menu.endHTML()

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
			                <input type="submit" value="Valider" />
			            </form>
			        </p>
			    </body>
			</html>
			"""



	@staticmethod
	def clean():
		return InteractBDD.deleteAll()


	def checkUserInput(self, user_input):
		if self.sanitization(user_input):
			if len(user_input)==2:
				Menu.currentStep=0
				
			if Menu.currentStep==0:
				Menu.userInput.append(user_input[0])
				Menu.userInput.append(user_input[1])
			else:
				Menu.userInput.append(user_input)

			if Menu.currentStep<3:
				Menu.currentStep+=1
			elif Menu.currentStep==3:
				Menu.currentStep=2


			
				output=str(eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")"))
				return output
		return "Looks like you tried to submit an empty value and succeeded, you can come back to login page now."
		

	def sanitization(self, user_input):
		forbiddenCharacters=["'", "\"", "\\", "&", "~", "{", "(", "[", "-", "|", "`", "_", "ç", "^", "à", "@", ")", "]", "=", "}", "+", "$", "£", "¤", "*", "µ", "ù", "%", "!", "§", ":", "/", ";", ".", ",", "?", "<", ">", "²"]
		if len(user_input)==0 or user_input=="": # empty input
			return False

		for elem in user_input:
			if len(elem)>=15: # max 15 characters
				return False

			for char in forbiddenCharacters: # no special characters
				if char in elem:
					return False
		return True
