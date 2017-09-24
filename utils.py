#coding: utf-8

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

