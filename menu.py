
from joueur import Joueur
from utils import Utils

class Menu(object):




	def __init__(self):
		print("")




	@staticmethod
	def showMenu():
		Utils.clear()
		print("Bonjour et bienvenu dans ce petit jeu! ;)\n")
		username = input ("Pouvez-vous indiquer votre nom d'utilisateur?")
		password = input ("Et votre mot de passe?")
		Joueur([username, password])