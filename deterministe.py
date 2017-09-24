import numpy
import math
import itertools
import utils
carte = [[0, 1, 2, 4, 3], [1, 0, 6, 9, 2], [2, 6, 0, 5, 7], [4, 9, 5, 0, 4],
         [3, 2, 7, 4, 0]]

NBVILLES = len(carte[0]) 
modele = numpy.arange(NBVILLES)
population = set()
population.add(tuple(modele))
#Generation de tout les chemins possibles
for perm in list(itertools.permutations(modele)):
    population.add(tuple(perm))

MEILLEURSCORE = math.inf
MEILLEURCHEMIN = None

def valabilite(chemin):
    global carte
    somme = 0
    paths = (utils.detail_path(chemin))
    #Parcours des couples de sommets
    for path in paths:
        for i in range(len(path) - 1):
            somme += carte[path[i]][path[i + 1]]
    return somme


def meilleurChemin():
    global MEILLEURSCORE, MEILLEURCHEMIN, population
    for chemin in population:
        if valabilite(chemin) < MEILLEURSCORE:
            MEILLEURSCORE = valabilite(chemin)
            MEILLEURCHEMIN = chemin

meilleurChemin()
print(MEILLEURSCORE, MEILLEURCHEMIN)
