                    #--------------------------------------#
                    #   Jeu des allumettes - Version 1.0   #
                    #        Player versus Computer        #
                    #--------------------------------------#

from random import *

# Paramètres de jeu
global nbrAllumettes# Nombres d'allumettes a definir par l'utilisateur
newAllumettes = 0
rounds = 0                # Numéro des tours du jeu
isGood = None             # Variable de verification de la réponse utilisateur
whoIsPlaying = None       # Variable de détermination de qui joue actuelement
playing = True            # Variable de gestion de la loop de jeu
actualPlayer = None       # Variable de determination de qui commence


def jeuDesAllumettes():

    # Menu d'explications du jeu
    def menu():

        global nbrAllumettes
        nbrAllumettes = 21

        print("-----------------------------------")
        print("|Bienvenue au jeu des allumettes !|")
        print("|  Voulez vous voir les règles ?  |")
        print("-----------------------------------")
        answer = input("[y/n]") # On demande a l'user s'il veut les règles

        # Verification de la réponse de l'utilisateur
        if answer == "n" or answer == "N":
            print("\n\nAlors bonne chance !\n\n\n\n\n\n\n\n")
            chooseStarter() # On passe à la suite du jeu (séléction starter)
        elif answer == "y" or answer == "Y":
            print("\n\nVoici les règles :\n")
            print("Un paquet d'allumettes est devant vous, chacun son tour,")
            print("chaque joueur va retirer 1, 2, 3 ou 4 allumettes.\n")
            print("Le joueur retirant la dernière allumette, perds la partie\n\n")
            print("BONNE CHANCE !\n\n\n\n\n\n\n\n")
            chooseStarter() # On passe à la suite du jeu (séléction starter)
        
    
    def chooseStarter():
        global nbrAllumettes

        playing = False
        actualPlayer = randint(0,1) # Selection du starter aléatoirement
        # Verification de qui commence (humain ou pas)
        if actualPlayer == 1:
            print("[GAME] - Le joueur humain commence !")
            print("[GAME] - Début du jeu :\n")
            tourJoueur()
        elif actualPlayer == 0:
            playing = False
            print("[GAME] - Le joueur non humain commence !")
            print("[GAME] - Début du jeu :\n")
            tourOrdi()


    # Verification de la réponse du joueur humain A CHANGER
    def checkAnswer():
        if newAllumettes > 1 and newAllumettes <= 4:
            return
        elif newAllumettes < 0 or newAllumettes > 4:
            print("Nombre incorect !")

            
    def tourJoueur():
        global nbrAllumettes

        if nbrAllumettes > 1:
            retire = int(input("Combiens d'allumettes voulez vous retirer ? (Entre 1 et 3) : "))
            #checkAnswer() #On verifie que la reponse est acceptable
            nbrAllumettes -= retire #On update le nombres d'allumettes restantes en fonction de la reponse

            #On affiche le nombres d'allumettes restantes dans le jeu
            print("\n\n")
            print("+-----------------------------------------+")
            print("| Il reste : " , nbrAllumettes ," allumettes !            |")
            print("+-----------------------------------------+")
            print("\n\n")

            tourOrdi() #On passe au tour de l'ordinateur
        elif nbrAllumettes <= 1:
            playing = False
            print("FIN DU JEU !")
            print("Joueur gagne")
            return

    def tourOrdi():
        global nbrAllumettes

        if nbrAllumettes > 1:
            print("L'ordinateur est en train de jouer...")
            retire = randint(1, 3)
            print("L'ordinateur retire " ,retire, "allumettes(s)")
            nbrAllumettes -= retire #On update le nombres d'allumettes restantes en fonction de la reponse

            #On affiche le nombres d'allumettes restantes dans le jeu
            print("\n\n")
            print("+-----------------------------------------+")
            print("| Il reste : " , nbrAllumettes ," allumettes !            |")
            print("+-----------------------------------------+")
            print("\n\n")

            tourJoueur() #On passe au tour du joueur
        elif newAllumettes <= 1:
            playing = False
            print("FIN DU JEU !")
            print("Ordinateur gagne")
            return

    


    def gameLoop():
        while playing:
            chooseStarter()
            
            
        

    menu()




                  

