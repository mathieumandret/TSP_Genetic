#coding: utf-8

import random

a = [1, 2, 3, 4]
b = [4, 1, 2, 3]

#TMX 2 points
#Si on garde l'intervale [0, len(a)], on peut avoir un
#point de découpe gauche a len(a), le tableau ne serait
#alors pas découpé
gauche = random.randint(0,len(a)-1)
droite = random.randint(0,len(a))

#Si l'interval n'est pas valable, recalculer la partie droite
while droite <= gauche:
    droite = random.randint(0,len(a))
print("gauche: ",gauche, "droite: ", droite)

#Swap
a[gauche:droite], b[gauche:droite] = b[gauche:droite], a[gauche:droite]

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
    return [
        el for el in chemin[gauche:droite]
        if el in (chemin[:gauche] + chemin[droite:])
    ] == []

    #Partie exterieure de la decoupe


partex = a[:gauche]+a[droite:] 
#Partie interieur de la decoupe
partint = a[gauche:droite]
dup = []

#Detection de l'indice des elements duplique
for i in range(len(partex)):
    if partex[i] in partint:
        dup.append(partex[i])

#Detection et reparation des elements dupliques

#TODO utiliser un while
for i in range(10):
    for i in range(len(partex)):
        #Si un element de la partie ext appartient aussi à  la partie interieure
        if partex[i] in partint:
            #On prends l'element correspondant dans le dictionnaire des échanges
            remp = echangesB[partex[i]]
            #On remplace l'element duplique par sa correspondance dans le dictionnaire des echanges
            partex[i] = remp

#On doit retrouver 3,1,2,4

res = []

print(partint)
print(partex)

indiceInte = 0
indiceExte = 0
for i in range(len(a)):
    if i < gauche:
        res.append(partex[indiceExte])
        indiceExte += 1
    elif i < droite:
        res.append(partint[indiceInte])
        indiceInte += 1
    else:
        res.append(partex[indiceExte])
        indiceExte += 1

print(res)
print(estLegal(res))
