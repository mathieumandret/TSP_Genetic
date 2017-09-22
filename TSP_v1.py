#coding: utf-8

import utils
import math
import numpy.random

"""
DONNEES GLOBALES

Definition de la carte de 4 villes avec les distances:
    1-2 = 1
    1-3 = 2
    1-4 = 4
    2-3 = 6
    2-4 = 9
    3-4 = 5

"""
carte = [
            [0,1,2,4],
            [1,0,6,9],
            [2,6,0,5],
            [4,9,5,0],
        ]
#Nombre de villes dans la carte
NBVILLES = len(carte[0])
EFFECTIF_INITIAL = 20
MEILLEURSCORE = math.inf
MEILLEURCHEMIN = None

"""
GENERATION DE LA POPULATION INITALE DE EFFECTIF_INITIAL INDIVIDUS
"""

population = set()
i = 0
while(len(population) < EFFECTIF_INITIAL):
    modele = numpy.arange(NBVILLES)
    numpy.random.shuffle(modele)
    #Cast en tuple pour permettre le add
    population.add(tuple(modele))
    i += 1

"""
CALCUL DE LA VALABILITE DE CHAQUE INDIVIDU
"""

def valabilite(chemin):
    somme = 0
    paths = (utils.detail_path(chemin))
    #Parcours des couples de sommets
    for path in paths:
        for i in range(len(path) - 1):
            somme += carte[path[i]][path[i] - 1]
    return somme

"""
SELECTION DU MEILLEUR INDIVIDU
"""

def meilleurChemin():
    global MEILLEURSCORE
    for chemin in population:
        if valabilite(chemin) < MEILLEURSCORE:
            MEILLEURSCORE = valabilite(chemin)
            MEILLEURCHEMIN = chemin
            
    

"""
SELECTION DE 2 INDIVIDU ALEATOIREMENT
"""

pere = list(population)[numpy.random.randint(len(population))]
mere = list(population)[numpy.random.randint(len(population))]

"""
CROISEMENT DES 2 INDIVIDUS
"""

#TODO Integrer crossover.py

