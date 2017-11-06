# coding: utf-8

from Population import Population
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


def animer(i):
    """
    Met à jour le graphe du meilleur chemin de chaque population
    """
    p1.evoluer(MUT_1)
    print(p1.generation)
    nx1, ny1 = p1.meilleurChemin.to_plot()
    graph1.set_data(nx1, ny1)


# Paramètres des populations
NBINDIVIDUS = 100
MUT_1 = 30

# Création de 2 populations identiques de 100 individus
p1 = Population(NBINDIVIDUS, 0, "cercle.csv")
# Meilleurs chemins des 2 population
x1, y1 = p1.meilleurChemin.to_plot()
# Préparation du graphe
fi = plt.figure()
plt.axes().set_aspect('equal', 'datalim')
# Affichage des villes
plt.scatter(x1, y1)
# Affichage du meilleur element deux populations
graph1, = plt.plot(x1, y1, 'r')
# Animation
ani = FuncAnimation(fi, animer, interval=10)
plt.show()
plt.close()
