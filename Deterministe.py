from Chemin import Chemin
from Ville import Ville
from csv import reader
from math import inf
from itertools import permutations
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

coords = []
with open('coords.csv', 'r') as f:
    r = reader(f)
    for x in r:
        coords.append(Ville(int(x[0]), int(x[1])))
carte = Chemin.from_array(coords)

chemins = []

score = inf
best = None


def toPlot(c):
    x = []
    y = []
    for coo in c:
        x.append(coo.x)
        y.append(coo.y)
    return x, y


#Generation de tout les chemins possibles
for perm in (permutations(carte)):
    chemins.append(Chemin.from_array(list(perm)))

for chemin in chemins:
    chemin.liste_villes.append(chemin.liste_villes[0])
    fit = chemin.fitness()
    if fit < score:
        score = fit
        best = chemin
x,y = toPlot(best)

fig = plt.figure()
plt.scatter(x,y)
plt.plot(x,y)
plt.show()

print(best)
print(score)

