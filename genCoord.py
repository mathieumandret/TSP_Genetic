#coding: utf-8

from random import randint
import csv

"""
Genere n coordonnées (x,y) et les ecrit dans le fichier coords.csv du repertoire courant
"""

#Dimensions de la carte
xmax = 500
ymax = 500

n = 10

coords = []

for i in range(n):
    coords.append((randint(0,xmax), randint(0,ymax)))

with open("coords.csv", 'w') as f:
    writer = csv.writer(f)
    writer.writerows(coords)


