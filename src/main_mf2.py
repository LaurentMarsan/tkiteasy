#coding: utf-8

from tkiteasy import *
from random import randint
from time import sleep

g = ouvrirFenetre(800,600)
h = ouvrirFenetre(80,60)

# for _ in range(3):
#     for _ in range(12):
#         g.dessinerDisque(randint(0,800),randint(0,600),randint(0,100),"pink")
#     g.actualiser()
#     g.attendreClic()
# #     g.supprimerTout()
# 
# for _ in range(3):
#     for _ in range(12):
#         h.dessinerDisque(randint(0,80),randint(0,60),randint(0,10),"pink")
#     h.actualiser()
# h.attendreClic()
# h.supprimerTout()
# g.attendreClic()
# g.supprimerTout()

while True:
    print(len(ObjetGraphique.annuaire))
    clich = h.recupererClic()
    clicg = g.recupererClic()
    if clich:
        if clich.num==1:
            h.dessinerDisque(clich.x,clich.y,randint(0,10),"pink")
        elif clich.num==3:
            obj = h.recupererObjet(clich.x,clich.y)
            if not obj:
                print("hnope")
            else:
                h.supprimer(obj)

    if clicg:
        if clicg.num==1:
            g.dessinerDisque(clicg.x,clicg.y,randint(0,100),"pink")
        elif clicg.num==3:
            obj = g.recupererObjet(clicg.x,clicg.y)
            if not obj:
                print("gnope")
            else:
                g.supprimer(obj)

    
#     time.sleep(0.2)
    g.pause(0.1)
print("dead")
sleep(1)




