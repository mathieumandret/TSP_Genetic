#coding: utf-8

import utils
import math
import numpy.random
from crossover import crossover
"""
DONNEES GLOBALES

Definition de la carte de 4 villes avec les distances:
    1-2 = 1
    1-3 = 2
    1-4 = 4
    2-3 = 6
    2-4 = 9
    3-4 = 5
    1-5 = 3
    2-5 = 2
    3-5 = 7
    4-5 = 4

"""
carte = [[0, 1, 2, 4, 3], [1, 0, 6, 9, 2], [2, 6, 0, 5, 7], [4, 9, 5, 0, 4],
         [3, 2, 7, 4, 0]]
#Nombre de villes dans la carte
NBVILLES = len(carte[0])  #Pour une carte de 4 villes, on a 4! = 24 chemins
EFFECTIF_INITIAL = 10
MEILLEURSCORE = math.inf
MEILLEURCHEMIN = None
"""
GENERATION DE LA POPULATION INITALE DE EFFECTIF_INITIAL INDIVIDUS
"""

population = set()
while (len(population) < EFFECTIF_INITIAL):
    modele = numpy.arange(NBVILLES)
    numpy.random.shuffle(modele)
    #Cast en tuple pour permettre le add
    population.add(tuple(modele))

#Repasser en liste pour eviter les casts
population = list(population)
for i in range(len(population)):
    population[i] = list(population[i])

"""
CALCUL DE LA VALABILITE DE CHAQUE INDIVIDU
"""

def valabilite(chemin):
    global carte
    somme = 0
    paths = (utils.detail_path(chemin))
    #Parcours des couples de sommets
    for path in paths:
        for i in range(len(path) - 1):
            somme += carte[path[i]][path[i + 1]]
    return somme


"""
SELECTION DU MEILLEUR INDIVIDU
"""


def meilleurChemin():
    global MEILLEURSCORE, MEILLEURCHEMIN, population
    for chemin in population:
        if valabilite(chemin) < MEILLEURSCORE:
            MEILLEURSCORE = valabilite(chemin)
            MEILLEURCHEMIN = chemin


"""
SELECTION DES MEILLEURS INDIVIDUS
"""


def meilleursIndividus(population, n):
    """
    Retourne les n meilleurs chemins
    de la population
    """
    meilleurs = []
    for i in range(n):
        meilleurs.append(sorted(population, key=valabilite)[i])
    return meilleurs


"""
EVOLUTION DE LA POPULATION
"""


def muter(chemin):
    """
    Echange la position de 2 elements dans
    un chemin
    """
    indice1 = numpy.random.randint(0, len(chemin) - 1)
    indice2 = numpy.random.randint(0, len(chemin) - 1)
    #Si les 2 indices sont identiques, recommencer
    while indice1 == indice2:
        indice2 = numpy.random.randint(0, len(chemin) - 1)
    chemin[indice2], chemin[indice1] = chemin[indice1], chemin[indice2]


def evoluer(population, freq_mut):
    """
    Selectionne les 10 meilleurs chemin
    les croise et remplace cette generation par la nouvelle
    en faisant potentiellement muter les chemin selon freq_mut
    """

    meilleurs = meilleursIndividus(population, 10)
    nouvelle_pop = []
    for i in range(len(meilleurs) - 1):
        e1, e2 = crossover((meilleurs[i]), (meilleurs[i + 1]))
        #Nombre aleatoire determinant si le chemin doit ou non muter
        r = numpy.random.randint(0, 100)
        #Simulation d'une probabilité de fre_mut de muter
        if r < freq_mut:
            muter(e1)
        r = numpy.random.randint(0, 100)
        if r < freq_mut:
            muter(e2)
        nouvelle_pop.append(e1)
        nouvelle_pop.append(e2)
    return nouvelle_pop

nbGen = 100
freq_mut = 20
meilleurChemin()
print(MEILLEURCHEMIN, MEILLEURSCORE)
for i in range(nbGen):
    population = evoluer(population, freq_mut)
    meilleurChemin()
    print(MEILLEURCHEMIN, MEILLEURSCORE)
