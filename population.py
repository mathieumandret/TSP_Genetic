from chemin import Chemin
from numpy import arange
from numpy.random import shuffle
from random import randint
import math

class Population:
    def __init__(self, nbInd, nbVilles):
        """
        Initialise une population de  nbInd chemins
        reliant nbVilles villes
        """
        self.individus = set()
        self.generation = 0
        self.bestScore = math.inf
        self.fittest = None      
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
        for ind in self.individus:
            if ind.fitness() < self.bestScore:
                self.bestScore = ind.fitness()
                self.fittest = ind
        return self.fittest, self.bestScore

    def orderByFitness(self):
        """
        Range les individus par score de fitness
        """
        self.individus.sort(key=lambda ind: ind.fitness())

    def __repr__(self):
        desc = ""
        desc += " Meilleur individu: " + str(self.getFittest()[0])
        desc += "\nMeilleur score: " + str(self.getFittest()[1])
        return desc

    def evolve(self, eff_new_gen, mut_rate):
        """
        Evolue la population courante en prenant
        eff_new_gen meilleurs individus
        """
        #Ranger la population avec les meilleurs individus en premier
        self.orderByFitness()
        #Tableau pour les n meilleurs individus
        bestInds = []
        #Nouvelle population
        new_pop = []
        print(len(self.individus))
        for i in range(eff_new_gen):
            bestInds.append(self.individus[i])
        for i in range(len(bestInds)-1):
            e1,e2 = bestInds[i].betterCrossover(bestInds[i+1])
            r = randint(0,100)
            if r < mut_rate:
                e1.mutate()
            r = randint(0,100)
            if r < mut_rate:
                e2.mutate()
            new_pop.append(e1)
            new_pop.append(e2)
        self.individus = new_pop
        self.generation +=1

