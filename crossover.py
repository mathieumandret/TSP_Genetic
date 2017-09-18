#coding: utf-8

import random

a = [1, 2, 3, 4]
b = [4, 1, 2, 3]

#TMX 2 points
gauche = 1
droite = 3

print(a,b)
#Swap
a[gauche:droite], b[gauche:droite] = b[gauche:droite],a[gauche:droite]

print(a,b)

#Echange effectues
echanges = {}
for i in range(len(b[gauche:droite])):
    echanges[a[gauche:droite][i]] = b[gauche:droite][i]
    echanges[b[gauche:droite][i]] = a[gauche:droite][i]

print(echanges)

#Verifier les elements dupliques et utiliser le dictionnaire echanges pour les corriger
