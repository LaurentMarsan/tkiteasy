#coding: utf-8
from tkiteasy import *

print("Cliquer pour faire défiler les polices, clic droit pour quitter")
g = ouvrirFenetre(800,1000)
pos = 50
for p in tkFont.families():
    g.afficherTexte(p,400,pos,"white",20, p)
    if pos>=950:
        pos = 0
        clic = g.attendreClic()
        if clic.num==3:
            g.fermerFenetre()
            exit()
        g.supprimerTout()
    pos += 50
g.attendreClic()
g.fermerFenetre()



