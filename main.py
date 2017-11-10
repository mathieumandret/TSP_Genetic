# coding: utf-8

from Population import Population
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import optparse

# Gestionnaire d'option
parser = optparse.OptionParser()
parser.add_option('-c', '--carte', action='store',
                  dest='carte', default='cercle.csv',
                  help='carte des villes à relier')
parser.add_option('-n', '--individus', action='store',
                  dest='nb_inds', default=50,
                  help='nombre d\'individus dans la population')
parser.add_option('-m', '--mutation', action='store',
                  dest='mut_rate', default=2,
                  help='fréquence de mutation')
parser.add_option('-g', '--generation', action='store',
                  dest='nb_gens', default=100,
                  help='nombre de générations')
parser.add_option('-t', '--tournoi', action='storeTrue', dest='sel_tournoi',
                  help='utiliser la méthode de selection par tournoi')
parser.add_option('-r', '--roulette', action='storeTrue', dest='sel_roulette',
                  help='utiliser la méthode de selection par roulette')
parser.add_option('-e', '--elitisme', action='storeTrue', dest='elitisme',
                  help='garder les meilleurs parents à chaque génération')

options, args = parser.parse_args()


def animer(i):
    """
    Met à jour le graphe du meilleur chemin de chaque population
    """
    p1.evoluer(options.mut_rate)
    nx1, ny1 = p1.meilleurChemin.to_plot()
    plt.title('Génération: ' + str(p1.generation))
    graph1.set_data(nx1, ny1)


p1 = Population(options.nb_inds, 0, options.carte)
init_dist = p1.meilleurFitness
x1, y1 = p1.meilleurChemin.to_plot()
fi = plt.figure()
plt.title('Génération: 1')
plt.axes().set_aspect('equal', 'datalim')
plt.scatter(x1, y1)
graph1, = plt.plot(x1, y1, 'r')
ani = FuncAnimation(fi, animer, interval=10, repeat=False,
                    frames=options.nb_gens - 2)
plt.show()
plt.close()
end_dist = p1.meilleurFitness
