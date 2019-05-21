from fractions import Fraction


def fraction():
    while 1:
        x = 0
        y = 0
        choix = int(input("(1) Approximation ou (2) Reduction (0 pour sortir)"))
        if choix == 1:
            x = float(input("De quel nombre voulez-vous la fraction? "))
            y = Fraction(x)
            print("L'approximation de votre nombre est ", y)
        elif choix == 2:
            x = input("De quelle fraction voulez-vous la réduction? ").split("/")
            y = Fraction(int(x[0]), int(x[1]))
            print("La réduction de votre fraction est ", y)
        elif choix == 0:
            return
