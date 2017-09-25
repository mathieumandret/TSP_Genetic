from chemin import Chemin
from population import Population

#coding: utf-8

from itertools import permutations
#Carte de  4 villes
carte = Chemin(5)
pop = []

#Generation de toutes les permutation possibles de la carte
for i in list(permutations(carte)):
    #Creation d'un chemin a partir de la permutation
    pop.append(Chemin.fromArray(i))

#Creation d'une population sur la base des permutations
p = Population.fromArray(pop)
print(p)
    

