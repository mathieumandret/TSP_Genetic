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
        self.individus = []
        self.generation = 0
        self.bestScore = math.inf
        self.fittest = None      
        carte = Chemin(nbVilles)
        self.individus.append(carte)
        #On peut déjà ajouter la carte comme un individu
        while len(self.individus) < nbInd:
            self.individus.append(carte.shuffle())

    @classmethod
    def fromArray(self, arr):
        p = Population(0,0)
        p.individus = arr
        return p

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
        desc += "Meilleur individu: " + str(self.getFittest()[0])
        desc += "\nMeilleur score: " + str(self.getFittest()[1])
        return desc

    def evolve(self,mut_rate):
        """
        Evolue la population courante en prenant
        eff_new_gen meilleurs individus
        """
        #Ranger la population avec les meilleurs individus en premier
        self.orderByFitness()
        #Nouvelle population
        new_pop = []
        if range(0, len(self.individus)-2,2) == (0,0):
            print("ERREUR")
        for i in range(0, len(self.individus)-2,2):
            #Creation de 2 enfants a partir de l'element courant et du suivant
            e1,e2 = self.individus[i].betterCrossover(self.individus[i+1])
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

