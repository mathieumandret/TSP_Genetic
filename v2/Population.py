#coding: utf-8

from Chemin import Chemin
from math import inf
from random import sample


class Population:
    """
    Represente une population de n chemins, tous composés des memes villes
    """

    def __init__(self, nbIndividus, nbVilles):
        """
        Initialise une population de nbIndividus, chemins reliant nbVilles
        """
        #Permet de suivre l'évolution
        self.generation = 1
        self.individus = []
        #Pour recuperer la meilleure fitness, on doit être sur
        #que le premiere valeur qu'on evalueara sera inférieure a meilleurFitness
        self.meilleurFitness = inf
        #Membre de la population de distance la plus courte, inexistant a l'initilisation
        self.meilleurChemin = None
        #Creation de la carte, qui est un chemi1n dont l'ordre n'importe pas, il sert de base a la
        #generation de la population
        carte = Chemin(nbVilles)
        #La carte est aussi un chemin valide, l'ajouter
        self.individus.append(Chemin.fromArray(carte))
        #Tant qu'on a pas atteint le nombre d'individus cible
        while len(self.individus) < nbIndividus:
            #On ajouter une permutation aléatoires de la carte a la population
            self.individus.append(
                Chemin.fromArray(sample(carte.liste_villes, len(carte))))

    def __repr__(self):
        """
        Retourne une représentation textuelle de la population
        """
        rep = ""
        for i in range(len(self)):
            rep += str(self.individus[i])
            rep += "\n"
        rep += str(self.meilleurFitness) + "\n"
        rep += str(self.meilleurChemin)
        rep += "\n"
        return rep

    def __len__(self):
        """
        Permet l'appel de len() sur une population
        """
        return len(self.individus)

    def eval(self):
        """
        Met a jour les valeur meilleurFitness et meilleurChemin
        """
        #Parcours de tous les chemins de la population
        for chemin in self.individus:
            #Enregistrement dans une variable de la fitness du chemin courant
            #pour eviter un double appel a chaque iteration
            fit = chemin.fitness()
            #Si le chemin courant a une meilleure fitness que le record actuel
            if fit < self.meilleurFitness:
                self.meilleurChemin = chemin
                self.meilleurFitness = fit


    def trierMeilleurs(self):
        """
        Trie la population en plaçant les chemins les plus courts en premier
        """
        #Tri avec pour cle la fonction fitness de Chemin
        self.individus.sort(key = lambda x: x.fitness())

    def evoluer(self, mut_freq):
        """
        Fait evoler la population vers une nouvelle generation,
        avec un taux de mutation de mut_freq
        """
        #tableau qui contiendra les fils de individus
        nouvelle_pop = []
        #Evaluation de la population
        self.eval()
        #Tri avec les meilleurs individus en premier
        self.trierMeilleurs()
        #Parcours des chemin, en les croisant un a un 
        for i in range(len(self.individus)-1):
            nouvelle_pop.append(self.individus[i].crossover(self.individus[i+1]))
        #Ajouter un croisement premier x deuxieme
        nouvelle_pop.append(self.individus[0].crossover(self.individus[1]))
        self.individus = nouvelle_pop
        self.generation += 1

            
        

        


