#coding: utf-8
"""
Un chemin est une liste de sommet (villes)
nb_indiv est le nombre de chemins à générer
nb_villes est le nombre d'element dans 1 chemin
"""

from itertools import permutations
from random import randint

def gen_perms(nb_chemins, nb_villes):
    """
    Generer nb_chemins permutations de nb_villes
    """
    chemins = []
    index = 0
    for i in permutations(range(nb_villes)):
        if index == nb_chemins:
            break
        chemins.append(i)
        index += 1
    return chemins

def mutate(chemin):
    """
    Fait muter un chemin en intervertissant 2 éléments aléaoirement
    """
    indice1 = randint(0, len(chemin)-1)
    indice2 = randint(0, len(chemin)-1)
    #Si les 2 indices sont identiques, recommencer
    while indice1 == indice2:
        indice2 = randint(0, len(chemin)-1)
    chemin[indice2], chemin[indice1] = chemin[indice1], chemin[indice2]

def potentially_mutate(prob, chemin):
    """
    Fait ou non muter un chemin selon une probabilité donnée
    """
    if randint(0,100) < prob:
        mutate(chemin)

def store_path_with_weight:
    """
    On chercher a representer un graphe pondéré
    """

