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
                  dest='nb_inds', default=50, type='int',
                  help='nombre d\'individus dans la population')
parser.add_option('-m', '--mutation', action='store',
                  dest='mut_rate', default=2, type='int',
                  help='fréquence de mutation')
parser.add_option('-g', '--generation', action='store',
                  dest='nb_gens', default=100, type='int',
                  help='nombre de générations')
parser.add_option('-t', '--tournoi', action='store_true', dest='sel_tournoi',
                  help='utiliser la méthode de selection par tournoi')
parser.add_option('-r', '--roulette', action='store_true', dest='sel_roulette',
                  help='utiliser la méthode de selection par roulette')
parser.add_option('-e', '--elitisme', action='store_true', dest='elitisme',
                  help='garder les meilleurs parents à chaque génération')

options, args = parser.parse_args()


def benchmark(pct_impr):
    """
    Ecrit le taux d'amélioration
    en fonction des paramètres courants
    dans un fichier
    """
    selection = 1 if options.sel_tournoi else 2
    elitisme = 1 if options.elitisme else 0
    # Formattages: nombre d'individus, nombre de generation, taux de mutation,
    # methode de selection, elitisme, pourcentage d'amélioration
    opts = '{0}, {1}, {2}, {3}, {4}, {5}\n'.format(
        options.nb_inds,
        options.nb_gens,
        options.mut_rate,
        selection,
        elitisme,
        pct_impr)

    with open('data.csv', 'a') as f:
        f.write(opts)


def animer(i):
    """
    Met à jour le graphe du meilleur chemin de chaque population
    """
    if options.sel_roulette:
        p1.evoluer_roulette(options.mut_rate)
    elif options.elitisme:
        p1.evoluer_garder_parent(10, options.mut_rate)
    else:
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
pct_impr = round(end_dist / init_dist * 100, 2)
benchmark(pct_impr)
