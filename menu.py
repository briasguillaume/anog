
from joueur import Joueur
from interactBDD import InteractBDD
from output import Output
import hashlib


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
		self._output=Output()

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

		self._output.reset()

		if validation:
			str(eval(Menu.steps[Menu.currentStep] + "(" + Menu.getParameters() + ")"))
		else:
			self._output.content+ "Looks like you tried to submit an empty value and succeeded, you can come back to login page now."



		return self._output.toBeDisplayed()
			





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
		self._joueur.goingToNextIsland(value, self._output)
		self.checkAliveForRecruitment()


	def checkAliveForRecruitment(self):
		if self._joueur.availableToFight:
			Menu.tempData=self._joueur.askForRecruitment(self._output)
		else:
			self._joueur.resetCrew()
			self._output.content+ "Ton équipage est mort, il va falloir recommencer du début pour devenir le roi des pirates. y/n"


	def choseThatPirate(self, value):
		self._joueur.recrutement(len(Menu.tempData), self._output, Menu.tempData, value)


		

		
	@staticmethod
	def showBDD():
		return InteractBDD.retrieveWholeDatabase()



	
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
			self._output.content+ "Wrong password, try again."
		self._joueur.showMenu(self._output)


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
