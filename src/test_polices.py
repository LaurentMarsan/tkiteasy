#coding: utf-8
from tkiteasy import *

print("Cliquer pour faire défiler les polices, clic droit pour quitter")
g = ouvrirFenetre(1000,1000)
pos = 50
for p in tkFont.families():
    print(p)
    g.afficherTexte(p+" --->",200,pos,"white",16)
    g.afficherTexte(p,600,pos,"white",20, p)
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



