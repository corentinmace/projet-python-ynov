#                       +---------------------------------+
#                       |         Nombres premiers        |
#                       |     Methode de la division      |
#                       | Fait avec amour pour Mr Palemro |
#                       +---------------------------------+

def premiers():
    answer = int(input("Entrez jusqu'ou voulez vous avoir la liste des nombres premiers : "))

    def main(n, p=[2,3,5]): # 2, 3, 5 sont les premiers nbrs premiers
        k = 3 #K est egal a 3 car on ne teste pas en dessous, 1 n'est pas premier et 2 n'as pas besoin d'etre testé
        while k <= n:
            i = 0
            while i < len(p):
                if p[i]*p[i] > k: #Le nombre est premier
                    p.append(k) # On ajoute K au tableau si le resultat precedent est supérieur a k
                    break
                if (k % p[i]) == 0: # Le nombre n'est pas premier
                    break
                i += 1
            k += 2
        return p

    print(main(answer))
