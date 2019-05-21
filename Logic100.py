from random import *


def Logic100():
    essai = int(input("En combien d'essais voulez vous jouer (1 à 5) ?"))
    x = randint(0, 100)
    r = x%2
    s = x%3
    t = x%5
    u = x%7
    for i in range(essai):
        print("Reste par 2=", r)
        print("Reste par 3=", s)
        print("Reste par 5=", t)
        print("Reste par 7=", u)
        result = int(input("Quelle est votre proposition ?"))
        if result == x:
            break
        print("Raté!")
    if result == x:
        print("Bien joué vous avez gagné!!")
    else :
        print(x)
    retry = input("Voulez vous réessayer ? (O ou N)")
    if retry == "O" or retry == "o":
        Logic100()
    elif retry == "N" or retry == "n":
        return
