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
    default=30,
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
#Coordonées du meilleur element
x, y = best.toPlot()

limite = 0

#Preparation du fichier de sortie
benchmarkX = []
benchmarkY = []

img = 'cercle36p' + str(options.nbInds) + ' inds ' + str(options.freq_mut) + '%mut ' + str(options.nbGens) + 'gens'

#Fonction d'animation du graphe
def animer(i):
    global limite
    if limite < options.nbGens:
        p.evoluer(options.freq_mut)
        best = p.meilleurChemin
        current = p.meilleurCourant
        plt.title('Generation: ' + str(p.generation) + ' Meilleur score: ' + str(p.meilleurFitness))
        nx, ny = best.toPlot()
        graph.set_data(nx, ny)
        benchmarkX.append(p.generation)
        benchmarkY.append(p.meilleurFitness)
        limite += 1


#Si on veut afficher le graphe
if options.graph:
    fig1 = plt.figure()
    plt.title('Generation: ' + str(p.generation) + '  Meilleur score: ' + str(p.meilleurFitness))
    #Affichage des points
    plt.scatter(x, y, color='red')
    #Affichage des lignes
    graph, = plt.plot(x, y)
    #Enregistrement de l'evolution de la fitness en fonction des générations
    benchmarkX.append(p.generation)
    benchmarkY.append(p.meilleurFitness)
    ani = FuncAnimation(fig1, animer, interval=20)
    plt.show()
    plt.close()
    #Enregistrement des valeurs de benchmarks dans des images
    plt.title('Distance en fonction de la génération\nIndividus=' + str(options.nbInds) + ' mutation: ' + str(options.freq_mut) + ' %')
    plt.plot(benchmarkX, benchmarkY)
    plt.xlabel('Génération')
    plt.ylabel('Distance')
    plt.savefig('benchmarks/' + img + '.png')

else:
    for i in range(options.nbGens):
        p.evoluer(options.freq_mut)
        best = p.meilleurChemin
        bestFitness = p.meilleurFitness
        print(p.generation)
        print(bestFitness)

