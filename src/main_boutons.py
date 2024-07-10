#coding: utf-8
from tkiteasy import *


g = ouvrirFenetre(800,600)
i = g.mkbox(200,300,10)
b = g.button("allo",100,500)
#     g.attendreClic()
input()
g.supprimer(i)
g.supprimer(b)
g.attendreClic()
g.fermerFenetre()
