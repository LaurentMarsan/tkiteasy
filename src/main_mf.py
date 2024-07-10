#coding: utf-8
from tkiteasy import *

###### ouverture de fenêtre
g = ouvrirFenetre(800,600)
h = ouvrirFenetre(300,300)

d1 = g.dessinerDisque(600,500,30,"grey")
d2 = h.dessinerDisque(600,500,30,"grey")

g.actualiser()
h.actualiser()
h.attendreClic()
h.fermerFenetre()

g.attendreClic()
g.fermerFenetre()
