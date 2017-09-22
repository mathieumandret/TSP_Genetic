from chemin import Chemin
from numpy import arange
from numpy.random import shuffle
from random import randint

class Population:

    def __init__(self, nbInd, nbVilles):
        #La carte est chemin quelconque pour lequel l'ordre de ses elements n'importe pas
        self.individus = set()
        self.generation = 0
        carte = Chemin(nbVilles)
        self.individus.add(carte)
        #On peut déjà ajouter la carte comme un individu
        while len(self.individus) < nbInd:
            self.individus.add(carte.shuffle())
        #On a plus besion de garantir l'unicité des chemin
        #et la liste devra être triée par la suite
        #Au besoin, on pourra recaster la liste en set
        #en risquant des pertes d'individus
        self.individus = list(self.individus)
        
    def getFittest(self):
        """
        Retourne l'indivdu a la fitness la plus elevee
        et son score
        """
        bestScore = 0
        fittest = None
        for ind in self.individus:
            if ind.fitness() > bestScore:
                bestScore = ind.fitness()
                fittest = ind
        return fittest, bestScore

    def orderByFitness(self):
        """
        Range les individus par score de fitness
        """
        self.individus.sort(key = lambda ind: ind.fitness())

    
    def __repr__(self):
        desc = "Population " + str(self.generation) + ":\n"
        for ind in self.individus:
            desc += str(ind) + "\n"
        return desc
            

    def evolve(self):
        """
        TODO: a partir de la liste d'individus triée, faire un crossover des meilleurs
        et reparer les fils, remplacer cette génération par la nouvelle
        incrementer le compteur de generation
        """
        self.orderByFitness()
        for i in range(len(self.individus)-1):
            #crossover(self.individus[i], self.individus[i+1]

        
            



