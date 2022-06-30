
from joueur import Joueur
from interactBDD import InteractBDD
import hashlib
from flask import url_for


class Menu(object):

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
		validation=self.checkUserInput(user_input)

		output={}
		if validation:
			output['team']=""
			output['content']=str(eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")"))
			output['map']=""
		else:
			output['team']=""
			output['content']="Looks like you tried to submit an empty value and succeeded, you can come back to login page now."
			output['map']=""

	
		
		return output
			





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


	
	def choseThatIsland(self, value):
		txt=self._joueur.goingToNextIsland(value)
		txt=txt+self.checkAliveForRecruitment()
		return txt


	def choseThatPirate(self, value):
		txt=self._joueur.recrutement(len(Menu.tempData), Menu.tempData, value)
		return txt


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
			return True
		return False
		

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
