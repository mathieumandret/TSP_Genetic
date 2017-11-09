# coding: utf-8

from Population import Population
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

parser = argparse.ArgumentParser(
    description='gere le fichier carte passé en argument.')
parser.add_argument('carte')
args = parser.parse_args()


def animer(i):
    """
    Met à jour le graphe du meilleur chemin de chaque population
    """
    p1.evoluer(MUT_1)
    nx1, ny1 = p1.meilleurChemin.to_plot()
    plt.title('Génération: ' + str(p1.generation))
    graph1.set_data(nx1, ny1)


# Paramètres des populations
NBINDIVIDUS = 50
MUT_1 = 5
NB_GENS = 1000
# Création de 2 populations identiques de 100 individus
p1 = Population(NBINDIVIDUS, 0, args.carte)
init_dist = p1.meilleurFitness
# Meilleurs chemins des 2 population
x1, y1 = p1.meilleurChemin.to_plot()
# Préparation du graphe
fi = plt.figure()
plt.title('Génération: 1')
plt.axes().set_aspect('equal', 'datalim')
# Affichage des villes
plt.scatter(x1, y1)
# Affichage du meilleur element deux populations
graph1, = plt.plot(x1, y1, 'r')
# Animation
ani = FuncAnimation(fi, animer, interval=10, repeat=False, frames=NB_GENS - 2)
plt.show()
plt.close()
end_dist = p1.meilleurFitness
