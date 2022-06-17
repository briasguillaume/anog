

from menu import Menu
menu= Menu()
menu.showMenu("")


'''
from equipage import Equipage
from pirate import Pirate
from utils import Utils
equipage1=Equipage([Pirate(50),Pirate(50),Pirate(50),Pirate(50)])
equipage2=Equipage([Pirate(50),Pirate(50),Pirate(50),Pirate(50)])

print(equipage1)
print(equipage2)

Utils.fight(equipage1,equipage2)
'''

'''
print("_______________")
from pirate import Pirate
from utils import Utils
from fruitdemon import FruitFactory

nom="trouduc"
level=5
qualite=0
fruit=FruitFactory.giveThatFruit("GumGum")
#print(fruit)
#print("_______________")

txt='{"type": "Pirate", "name": \"'+str(nom)+'\", "level": '+str(level)+ ', "qualite": '+str(qualite)+', "fruit": '+ str(fruit)+', "stats": '+str(Pirate.generateStats(level, qualite, fruit.power))+', "availableToFight": "True", "mort": "False"}'
#print(txt)
#print("_______________")

pirate=Utils.load(txt)
print(pirate)
print("_______________")

print(pirate.fruit)
print("_______________")

pirate.regenerateHealth(pirate.level, pirate.qualite)
'''

