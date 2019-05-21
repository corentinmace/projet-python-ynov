from Logic100 import Logic100
from Fraction import fraction
from TirageDeCarte import carte
from Lancer import Lancer
from Triangles import triangles
from Rect import rectangles
from NombresPremiers import premiers
from AllumetesGame import jeuDesAllumettes


def main():
    while 1:
        voir = input("1. Logic100 \n2. Tirage de cartes \n3. Fractions \n4. "
                     "Lancer de dès \n5. Triangles \n6. Rectangles \n7. Premiers \n8. Allumettes \n(S pour sortie) "
                     "\nQuel exercice voulez-vous voir ? ")

        if voir == "1":
            Logic100()
        elif voir == "2":
            carte()
        elif voir == "3":
            fraction()
        elif voir == "4":
            Lancer()
        elif voir == "5":
            triangles()
        elif voir == "6":
            rectangles()
        elif voir == "7":
            premiers()
        elif voir == "8":
            jeuDesAllumettes()
        elif voir == "s" or voir == "S":
            return


if __name__ == "__main__":
    main()

