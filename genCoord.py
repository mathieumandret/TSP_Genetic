#coding: utf-8

from random import randint
import csv
import sys

"""
Genere n coordonnées (x,y) et les ecrit dans le fichier coords.csv du repertoire courant
"""

#Dimension de la carte
dim = int(sys.argv[1])

#Nombre de villes
n = int(sys.argv[2])

#Fichier de destination
dest = sys.argv[3]

#Dimensions de la carte
xmax, ymax = dim, dim

coords = []

for i in range(n):
    coords.append((randint(0,xmax), randint(0,ymax)))

with open(dest,'w') as f:
    writer = csv.writer(f)
    writer.writerows(coords)
