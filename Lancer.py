from random import *


def Lancer():
    var = int (input ("Combien de dès voulez-vous lancer ? "))
    for i in range(var):
        x = randint(1, 6)
        print(x)
