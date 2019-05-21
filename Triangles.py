from tkinter import *
from random import *


def triangles():
    canvas_width = 500
    canvas_height =500

    master = Tk()

    w = Canvas(master, width=canvas_width, height=canvas_height)
    w.pack()

    taille = int(input("Voulez-vous un triangle grand (1), moyen (2), ou petit (3) ? "))

    if taille==1 :
        points = [5,0,uniform(canvas_width,canvas_width-canvas_width/3),canvas_height/2, 5, uniform(canvas_height, canvas_height-canvas_height/3)]
    elif taille==2:
        points = [5,0,uniform(canvas_width/3,canvas_width-canvas_width/3),canvas_height/4, 5, uniform(canvas_height/3, canvas_height-canvas_height/3)]
    elif taille==3:
        points = [5,0,uniform(canvas_width/3,0),canvas_height/8, 5, uniform(canvas_height/3, 0)]

    couleur = input("De quelle couleur voulez-vous votre triangle (en anglais) ? ")
    pointillé = int(input("Voulez-vous un trait plein (1), des tirets (2), ou des pointillés (3) ? "))

    if pointillé == 1:
        w.create_polygon(points, fill='', outline=couleur)
    elif pointillé == 2:
        traits = [5, 2]
        w.create_polygon(points, fill='', outline=couleur, dash=traits)
    elif pointillé == 3:
        traits = [1,]
        w.create_polygon(points, fill='', outline=couleur, dash=traits)

    mainloop()
triangles()