#coding: utf-8

import random

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [3, 7, 5, 1, 6, 8, 2, 4]


def swap(chemin1, chemin2):
    """
    Echange une partie d'un
    chemin avec celle d'un autre
    selon 2 points de decoupe
    """
    chemin1[gauche:droite], chemin2[gauche:droite] = chemin2[
        gauche:droite], chemin1[gauche:droite]


def estLegal(chemin):
    """
    Verifie si un chemin contient ou non
    des elements dupliques
    """
    return len(chemin) == len(set(chemin))


def decouper(chemin, gauche, droite):
    """
    Pour un chemin complet retourne
    la partie interieure et exterieure
    aux points de découpe
    """
    #Partie exterieure de la decoupe
    partex = chemin[:gauche] + chemin[droite:]
    #Partie interieur de la decoupe
    partint = chemin[gauche:droite]
    return partint, partex


def recoller(partie_interieure, partie_exterieure, gauche, droite):
    """
    Prends en paramètres la partie interieure
    et exterieure d'un tableau et le reconstitue
    selon les points de decoupe
    """
    res = []
    indiceInte = 0
    indiceExte = 0
    for i in range(len(partie_exterieure) + len(partie_interieure)):
        #Si l'indice est strictement inférieur a gauche,
        #on ajoute un élément de l'exterieur
        if i < gauche:
            res.append(partie_exterieure[indiceExte])
            indiceExte += 1
        #Si il est superieur ou egal a droite, on est aussi a l'exterieur
        #des points de decoupe, on ajouter alors un element de l'exterieur
        elif i >= droite:
            res.append(partie_exterieure[indiceExte])
            indiceExte += 1
        #Si l'indice est superieur ou egal a gauche et strictement inférieur a droite
        #on se situe dans la découpe.
        else:
            res.append(partie_interieure[indiceInte])
            indiceInte += 1
    return res


#Detection et reparation des elements dupliques
def reparer(partint, partex, echanges, gauche, droite):
    while (estLegal(recoller(partint, partex, gauche, droite))) == False:
        print("Reparation...")
        for i in range(len(partex)):
            #Si un element de la partie ext appartient aussi à  la partie interieure
            if partex[i] in partint:
                #On prends l'element correspondant dans le dictionnaire des échanges
                remp = echanges[partex[i]]
                #On remplace l'element duplique par sa correspondance dans le dictionnaire des echanges
                partex[i] = remp


def crossover(chemin1, chemin2):
    #Selection aléatoire de 2 points de découpe
    gauche = random.randint(0, len(chemin1) - 1)
    droite = random.randint(0, len(chemin1))
    #Si l'intervale n'est pas valable, recalculer la partie droite
    while droite <= gauche:
        droite = random.randint(0, len(chemin1))
    #Echange des chemin en fonction des points de decoupe
    chemin1[gauche:droite], chemin2[gauche:droite] = chemin2[gauche:droite], chemin1[gauche:droite]
    #Enregistrement des echanges effectues
    echangesB = {}
    echangesA = {}
    for i in range(len(chemin2[gauche:droite])):
        echangesA[chemin1[gauche:droite][i]] = chemin2[gauche:droite][i]

    for i in range(len(chemin1[gauche:droite])):
        echangesB[chemin2[gauche:droite][i]] = chemin1[gauche:droite][i]
    #Decoupage des chemins
    partintA, partexA = decouper(chemin1, gauche, droite)
    partintB, partexB = decouper(chemin2, gauche, droite)
    #Reparation des chemins
    reparer(partintA, partexA, echangesA, gauche, droite)
    reparer(partintB, partexB, echangesB, gauche, droite)
    resA = recoller(partintA, partexA, gauche, droite)
    resB = recoller(partintB, partexB, gauche, droite)
    return resA, resB

print(a,b)
print(crossover(a,b))
#EFFET DE BORD
print(a,b)
