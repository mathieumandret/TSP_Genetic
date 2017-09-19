#coding: utf-8

import random

a = [1, 2, 3, 4]
b = [4, 1, 2, 3]

#TMX 2 points
gauche = 1
droite = 3

#Swap
a[gauche:droite], b[gauche:droite] = b[gauche:droite],a[gauche:droite]

#Echange effectues
echangesB = {}
echangesA = {}

for i in range(len(b[gauche:droite])):
    echangesB[a[gauche:droite][i]] = b[gauche:droite][i]

for i in range(len(a[gauche:droite])):
    echangesA[b[gauche:droite][i]] = a[gauche:droite][i]

def estLegal(chemin):
    """
    Verifie si un chemin contient ou non 
    des elements dupliques
    """
    return [el for el in chemin[gauche:droite] if el in (chemin[:gauche]+chemin[droite:])] == []

#Partie exterieure de la decoupe
partex = a[::(droite-gauche)+1] # = a[:gauche]+a[droite:]
#Partie interieur de la decoupe
partint = a[gauche:droite]

print(partex, partint)

dup = []

#Detection de l'indice des elements duplique
for i in range(len(partex)):
    if partex[i] in partint:
        dup.append(partex[i])

print("Elements dupliques: ",dup)
print("A remplacer par", echangesB[dup[0]])


