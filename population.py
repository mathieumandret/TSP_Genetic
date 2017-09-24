from chemin import Chemin
from numpy import arange
from numpy.random import shuffle
from random import randint
import math
from crossover import crossover


class Population:
    def __init__(self, nbInd, nbVilles):
        """
        Initialise une population de  nbInd chemins
        reliant nbVilles villes
        """
        #La carte est chemin quelconque pour lequel l'ordre de ses elements n'importe pas
        self.individus = set()
        self.generation = 0
        carte = Chemin(nbVilles)
        self.individus.add(carte)
        #On peut déjà ajouter la carte comme un individu
        while len(self.individus) < nbInd:
            self.individus.add(carte.shuffle())
        self.individus = list(self.individus)

    def getFittest(self):
        """
        Retourne l'indivdu a la fitness la plus elevee
        et son score
        """
        bestScore = math.inf
        fittest = None
        for ind in self.individus:
            if ind.fitness() < bestScore:
                bestScore = ind.fitness()
                fittest = ind
        return fittest, bestScore

    def orderByFitness(self):
        """
        Range les individus par score de fitness
        """
        self.individus.sort(key=lambda ind: ind.fitness())

    def __repr__(self):
        desc = "Population " + str(self.generation) + ":\n"
        for ind in self.individus:
            desc += str(ind) + "\n"
        desc += " Meilleur individu: " + str(self.getFittest()[0])
        desc += "\nMeilleur score: " + str(self.getFittest()[1])
        return desc

    def evolve(self, eff_new_gen):
        """
        Evolue la population courante en prenant
        eff_new_gen meilleurs individus
        """
        self.orderByFitness()
        bestInds = []
        new_pop = []
        #On place les meilleurs chemins dans un tableau
        for i in range(eff_new_gen):
            bestInds.append(self.individus[i])
        for i in range(len(bestInds)-1):
            a1, a2 = crossover(bestInds[i], bestInds[i+1])
            new_pop.append(a1)
            new_pop.append(a2)
        self.individus = new_pop
        self.generation += 1
    
            
            
