import numpy.random

def detail_path(string_path):
    """
    Prends en paramètre une chaine de caractère du type
    '1234' retourne le parcours de sommet en sommet
    [['1','2'], ['2','3'], ['3','4']]
    """
    glob_list = []
    i = 0
    while (i < len(string_path) - 1):
        tmp_list = [int(string_path[i]), int(string_path[i + 1])]
        glob_list.append(tmp_list)
        i += 1
    return glob_list


def init_map():
    """
    Cree une matrice d'incidence du graphe
    de la carte de villes
    """
    return [[-1, 1, 2], [1, -1, 4], [2, 4, -1]]


def get_weight(string_path):
    """
    Retourne le poids d'un chemin donne
    par un string de la forme '1234'
    """
    somme = 0
    #Pour paire de sommets, on doit ajouter a la somme
    #la valeur de matrix[sommet1-1][sommet2-1]

    matrix = init_map()
    weight = 0
    paths = (detail_path(string_path))
    #Parcours des couples de sommets
    for path in paths:
        for i in range(len(path) - 1):
            somme += matrix[path[i] - 1][path[i - 1] - 1]
    return somme


def crossover(p1, p2):
    """
    Cree une nouvelle liste a partir de
    2 listes parentes
    """
    #Selection des points de decoupe
    #Decoupe du deuxieme element au 3eme
    print(p1, "\n", p2, "\n\n")
    point_initial = 1
    point_final = 3
    child = p1
    child[point_initial:point_final] = p2[point_initial:point_final]
    print(child)
    #Elimination des elements dupliques
    s_child = set(child)
    print(s_child)

crossover([1,2,3,4],[5,6,7,8])



