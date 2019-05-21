from random import shuffle


def carte():
    L_couleurs = ['coeur', 'carreau', 'pique', 'trèfle']
    L_figures = ['as', 'roi', 'dame', 'valet',2,3,4,5,6,7,8,9,10]
    pioche = []
    for couleur in L_couleurs:
        for elt in L_figures:
            pioche.append([elt, couleur])
    shuffle(pioche)
    nb = int(input("Combien de cartes voulez-vous tirer ?"))
    for i in range (nb):
        print(pioche[0])
        pioche.remove(pioche[0])



