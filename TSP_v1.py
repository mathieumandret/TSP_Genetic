import utils
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

"""
GENERATION DE LA POPULATION INITALE DE 20 INDIVIDUS
"""

#TODO Garantir l'unicite de chaque individu (set)

EFFECTIF_INITIAL = 20
population = []
for i in range(EFFECTIF_INITIAL):
    modele = numpy.arange(NBVILLES)
    numpy.random.shuffle(modele)
    population.append(modele)


"""
CALCUL DE LA VALABILITE DE CHAQUE INDIVIDU
"""

def valabilite(chemin):
    somme = 0
    weight = 0
    paths = (utils.detail_path(chemin))
    #Parcours des couples de sommets
    for path in paths:
        for i in range(len(path) - 1):
            somme += carte[path[i]][path[i] - 1]
    return somme


"""
SELECTION DE 2 INDIVIDU ALEATOIREMENT
"""

pere = population[numpy.random.randint(len(population))]
mere = population[numpy.random.randint(len(population))]

"""
CROISEMENT DES 2 INDIVIDUS
"""

#TODO Implémenter le crossover


