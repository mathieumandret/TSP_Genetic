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

def swap(chemin1, chemin2):
    """
    Echange une partie d'un
    chemin avec celle d'un autre
    selon 2 points de decoupe
    """
    chemin1[gauche:droite], chemin2[gauche:droite] = chemin2[gauche:droite], chemin1[gauche:droite]


#Swap
swap(a,b)

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
    return len(chemin) == len(set(chemin))


def decouper(chemin):
    """
    Pour un chemin complet retourne 
    la partie interieure et exterieure
    aux points de découpe
    """
    #Partie exterieure de la decoupe
    partex = chemin[:gauche]+chemin[droite:] 
    #Partie interieur de la decoupe
    partint = chemin[gauche:droite]
    return partint, partex

partintA, partexA = decouper(a)
partintB, partexB = decouper(b)

def recoller(partie_interieure, partie_exterieure):
    """
    Prends en paramètres la partie interieure
    et exterieure d'un tableau et le reconstitue
    selon les points de decoupe
    """
    res = []
    indiceInte = 0
    indiceExte = 0
    for i in range(len(partie_exterieure)+len(partie_interieure)):
        if i < gauche:
            res.append(partie_exterieure[indiceExte])
            indiceExte += 1
        elif i < droite:
            res.append(partie_interieure[indiceInte])
            indiceInte += 1
        else:
            res.append(partie_exterieure[indiceExte])
            indiceExte += 1
    return res


#Detection et reparation des elements dupliques
def reparer(partint, partex, echanges):
    while (estLegal(recoller(partint,partex))) == False:
        for i in range(len(partex)):
            #Si un element de la partie ext appartient aussi à  la partie interieure
            if partex[i] in partint:
                #On prends l'element correspondant dans le dictionnaire des échanges
                remp = echanges[partex[i]]
                #On remplace l'element duplique par sa correspondance dans le dictionnaire des echanges
                partex[i] = remp

reparer(partintA, partexA, echangesB)
reparer(partintB, partexB, echangesA)

print(recoller(partintA, partexA))
print(recoller(partintB, partexB))
