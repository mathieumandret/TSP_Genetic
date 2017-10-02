#coding: utf-8

from Chemin import Chemin
from random import sample, randint, uniform
from copy import deepcopy
import pdb


class Population:
    """
    Represente une population de n chemins, tous composés des memes villes
    """

    def __init__(self, nbIndividus, nbVilles, csv=None):
        """
        Initialise une population de nbIndividus, chemins reliant nbVilles
        """
        #Permet de suivre l'évolution
        self.generation = 1
        self.individus = []
        #Pour recuperer la meilleure fitness, on doit être sur
        #que le premiere valeur qu'on evalueara sera inférieure a meilleurFitness
        #On pourrait utiliser math.inf disponible en 3.5
        self.meilleurFitness = 0
        #Membre de la population de distance la plus courte, inexistant a l'initilisation
        self.meilleurChemin = None
        #generation de la population
        if csv != None:
            carte = Chemin.fromCSV(csv)
        else:
            #Creation de la carte, qui est un chemin dont l'ordre n'importe pas, il sert de base a la
            carte = Chemin(nbVilles)
        #La carte est aussi un chemin valide, l'ajouter
        #self.individus.append(Chemin.fromArray(carte))
        self.individus.append(carte)
        #Tant qu'on a pas atteint le nombre d'individus cible
        while len(self.individus) < nbIndividus:
            #On ajouter une permutation aléatoires de la carte a la population
            self.individus.append(
                Chemin.fromArray(sample(carte.liste_villes, len(carte))))

        #On veut associer a chaque chemin sa valeur de fitness pour ne pas avoir a la
        #recalculer a chaque evaluation
        self.cache_fitness = {}
        #Meilleur chemin de la generation courante
        self.meilleurCourant = None


    def __repr__(self):
        """
        Retourne une représentation textuelle de la population
        """
        return str(self.meilleurFitness)

    def __len__(self):
        """
        Permet l'appel de len() sur une population
        """
        return len(self.individus)

    def eval(self):
        """
        Met a jour les valeur meilleurFitness et meilleurChemin
        """
        self.trierMeilleurs()
        self.meilleurCourant = self.individus[0]
        #Reinitialisation de la fitness total
        self.totalFitness = 0
        #Parcours de tous les chemins de la population
        for chemin in self.individus:
            #Les chemins reviennent tous a leur point de depart, mais on ne peut pas avoir de doublon dans un chemin
            #On doit donc rajouter la premiere ville à la fin de la liste au moment de l'evaluation pour avoir
            #une distance correcte, mais si on modifie le chemin, il ne pourra plus etre croisé avec un autre, puisqu'il
            #contiendra des doublons, on fait donc une copie a laquelle on rajoute la premier ville
            cp = deepcopy(chemin)
            cp.liste_villes.append(chemin[0])
            #Si la valeur de fitness existe dans le cache, la recuperer
            if chemin in self.cache_fitness:
                fit = self.cache_fitness[chemin]
            #Sinon l'ajouter au cache
            else:
                fit = cp.fitness()
                self.cache_fitness[chemin] = fit
            #Ajouter la fitness de l'objet courant au total
            self.totalFitness += fit
            #Si le chemin courant a une meilleure fitness que le record actuel
            if fit > self.meilleurFitness:
                self.meilleurChemin = cp
                self.meilleurFitness = fit

    def trierMeilleurs(self):
        """
        Trie la population en plaçant les chemins les plus courts en premier
        """
        #Tri avec pour cle la fonction fitness de Chemin
        self.individus.sort(key=lambda x: x.fitness())

    def selection(self):
        """
        Selectionne un individus de la population en fonction de leur fitness
        La fonction eval doit toujours avoir été appellée pour la génération courante
        avant cette fonction
        """
        i = 0
        #pdb.set_trace()
        ran = uniform(0, self.totalFitness)
        while (ran > 0):
            ran -= self.cache_fitness[self.individus[i]]
            i += 1
        i -= 1
        return self.individus[i]

    def selectionParTournoi(self, n):
        """
        A partir d'un echantillon aléatoire de n individus, selectionne le meilleur
        """
        #Selection de n membre de la population
        participants = sample(self.individus, n)
        #Recherche du meilleur participant
        participants.sort(key=lambda x: x.fitness())
        #Selection du meilleur participant
        return participants[len(participants)-1]

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
        #self.trierMeilleurs()
        #Pour chaque element de la population parente
        for i in range(len(self.individus)):
            fils = self.selectionParTournoi(5).crossover(self.selectionParTournoi(5))
            r = randint(0, 100)
            if r < mut_freq:
                fils.muter()
            nouvelle_pop.append(fils)
        #Remplacer l'ancienne population par la nouvelle
        self.individus = nouvelle_pop
        self.generation += 1
