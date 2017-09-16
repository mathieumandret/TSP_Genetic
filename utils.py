def detail_path(string_path):
    """
    Prends en paramètre une chaine de caractère du type
    '1234' retourne le parcours de sommet en sommet
    [['1','2'], ['2','3'], ['3','4']]
    """
    glob_list = []
    i = 0
    while(i < len(string_path)-1):
        tmp_list = [int(string_path[i]), int(string_path[i+1])]
        glob_list.append(tmp_list)
        i += 1
    return glob_list

def init_map():
    """
    Cree une matrice d'incidence du graphe 
    de la carte de villes
    """
    return [[-1,1,2], [1,-1,4], [2,4,-1]]

def get_weight(string_path):
    """
    Retourne le poids d'un chemin donne
    par un string de la forme '1234'
    """

    #Pour paire de sommets, on doit ajouter a la somme 
    #la valeur de matrix[sommet1-1][sommet2-1]

    matrix = init_map()
    weight = 0
    paths = (detail_path(string_path))
    for path in paths:
        print(path)

#Cette fonction devrai retourner
# 1->2 2->3
# 1 + 4 = 5
get_weight('123')
