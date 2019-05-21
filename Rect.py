from tkinter import *


def rectangles():
    tailleBitmap = 0
    i = 0
    canvas_width = 500
    canvas_height =500

    master = Tk()

    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()

    couleur = input("De quelle couleur est votre dessin ? (en anglais)")

    longeur =  int(input("De quelle longeur est votre rectangle ? "))
    largeur =  int(input("De quelle largeur est votre rectangle ? "))

    bitmap = int(input("Quel motif souhaitez-vous ? \n1. Pas de motif \n2. Hachures verticales \n3. Hachures "
                       "horizontales"))
    w.create_rectangle(50, 50, 50 + longeur, 50 + largeur, fill='', outline=couleur)

    if bitmap == 2:
        tailleBitmap = int(input("Entrez l'écartement des hachures"))
        while tailleBitmap*i < longeur:
            w.create_line(50 + tailleBitmap * i, 50, 50 + tailleBitmap * i, 50 + largeur, fill=couleur)
            i+=1
    elif bitmap == 3:
        tailleBitmap = int(input("Entrez l'écartement des hachures"))
        while tailleBitmap*i < largeur:
            w.create_line(50, 50 + tailleBitmap * i, 50 + longeur, 50 + tailleBitmap * i, fill=couleur)
            i+=1


    mainloop()


