#coding: utf-8

from Population import Population
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import optparse

#Gestionnaire de parametres
parser = optparse.OptionParser()

parser.add_option(
    '-g',
    '--graph',
    action='store_true',
    dest='graph',
    default=False,
    help='Affiche un graphe des chemins')

parser.add_option(
    '-f',
    '--fichier',
    action='store',
    dest='fichier_csv',
    default=None,
    help='Fichier CSV depuis lequel lire les coordoonnées des villes')

parser.add_option(
    '-n',
    '--nbVilles',
    action='store',
    dest='nbVilles',
    default=20,
    type='int',
    help='Nombre de villes a generer')

parser.add_option(
    '-m',
    '--mutation',
    action='store',
    dest='freq_mut',
    default=10,
    type='int',
    help='Frequence de mutation')

parser.add_option(
    '-i',
    '--individus',
    action='store',
    dest='nbInds',
    default=7,
    type='int',
    help='Nombre d\'individus dans la population')


parser.add_option(
    '-l',
    '--limite',
    action='store',
    dest='nbGens',
    default=5000,
    type='int',
    help='Nombre de generations')

#Recuperation des parametres
options, a = parser.parse_args()

#Gestion des options incompatibles
#Si on fourni un fichier csv, on ne peut pas choisir le nombre de villes
if options.nbVilles != 20 and options.fichier_csv != None:
    print(
        'Vous ne pouvez pas choisir le nombre de villes si vous charger un fichier csv'
    )
    quit()

#Si on a specifie un fichier, charger la carte a partir de celui-ci
if options.fichier_csv != None:
    p = Population(options.nbInds, 0, options.fichier_csv)
#Sinon, generer les villes aléatoirement
else:
    p = Population(options.nbInds, options.nbVilles)
#Evaluation initiale de la population
p.eval()
#Recuperation du meilleur element
best = p.meilleurChemin
current = p.meilleurCourant
#Coordonées du meilleur element
x, y = best.toPlot()
cx, cy = current.toPlot()

limite = 0

#Fonction d'animation du graphe
def animer(i):
    global limite
    if limite < options.nbGens:
        p.evoluer(options.freq_mut)
        best = p.meilleurChemin
        current = p.meilleurCourant
        plt.title('Generation: ' + str(p.generation) + ' Meilleur score: ' + str(p.meilleurFitness))
        nx, ny = best.toPlot()
        ncx, ncy = current.toPlot()
        graph.set_data(nx, ny)
        graph2.set_data(ncx, ncy)
        limite += 1


#Si on veut afficher le graphe
if options.graph:
    fig1, axarr = plt.subplots(2)
    plt.title('Generation: ' + str(p.generation) + ' Meilleur score: ' + str(p.meilleurFitness))
    #Affichage des points
    axarr[0].scatter(x, y, color='red')
    axarr[1].scatter(x, y, color='red')
    #Affichage des lignes
    graph, = axarr[0].plot(x, y,)
    graph2, = axarr[1].plot(cx, cy)
    ani = FuncAnimation(fig1, animer, interval=20)
    plt.show()

else:
    for i in range(options.nbGens):
        p.evoluer(options.freq_mut)
        best = p.meilleurChemin
        bestFitness = p.meilleurFitness
        print(p.generation)
        print(bestFitness)
