from Chemin import Chemin
from Ville import Ville
from math import inf
from itertools import permutations

coords = [Ville(1,2), Ville(3,7), Ville(12, 2), Ville(11, 9), Ville(10,1)]
carte = Chemin.fromArray(coords)

chemins = []

score = inf
best = None

#Generation de tout les chemins possibles
for perm in (permutations(carte)):
    chemins.append(Chemin.fromArray(list(perm)))

for chemin in chemins:
    fit = chemin.fitness()
    if fit < score:
        score = fit
        best = chemin
    print(score, best)
        
        





