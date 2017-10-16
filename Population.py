#coding: utf-8

from Chemin import Chemin
from random import sample, randint, uniform
from math import inf
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
        self.meilleurFitness = inf
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
        #Evaluation de la population
        self.eval()

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
        #Parcours de tous les chemins de la population
        for chemin in self.individus:
            #TODO utiliser un cache pour les chemin connus
            ferme = chemin.liste_villes + chemin.liste_villes[-1:]
            fit = Chemin.fromArray(ferme).fitness() 
            #Si le chemin courant a une meilleure fitness que le record actuel
            if fit < self.meilleurFitness:
                self.meilleurChemin = Chemin.fromArray(ferme)
                self.meilleurFitness = fit  

    def trierMeilleurs(self):
        """
        Trie la population en plaçant les chemins les plus courts en premier
        """
        #Tri avec pour cle la fonction fitness de Chemin
        self.individus.sort(key=lambda x: x.fitness())

    def selectionParRoulette(self):
        """
        Utilise la selection par roulette pour generer n nouveau individus
        """
        #Calcul de la fitness total
        total = 0
        i = 0
        for chemin in self.individus:
            total += 1/chemin.fitness()
        r = uniform(0,total) 
        while(r > 0):
            r -= 1/self.individus[i].fitness()
            i+=1
        return self.individus[i-1]

    def selectionParTournoi(self, n):
        """
        A partir d'un echantillon aléatoire de n individus, selectionne le meilleur
        """
        #Selection de n membre de la population
        participants = sample(self.individus, n)
        #Recherche du meilleur participant
        participants.sort(key=lambda x: x.fitness())
        #Selection du meilleur participant, qui a donc la plus petite valeur de fitness
        return participants[0]

    def evoluer(self, mut_freq):
        """
        Fait evoluer la population vers une nouvelle generation,
        avec un taux de mutation de mut_freq
        """
        #tableau qui contiendra les fils de individus
        nouvelle_pop = []
        #Tri avec les meilleurs individus en premier
        #self.trierMeilleurs()
        #Pour chaque element de la population parente
        for i in range(len(self.individus)):
            fils = self.selectionParTournoi(10).crossover(self.selectionParTournoi(10))
            r = randint(0, 100)
            if r < mut_freq:
                fils.muter()
            nouvelle_pop.append(fils)
        #Remplacer l'ancienne population par la nouvelle
        self.individus = nouvelle_pop
        self.eval()
        self.generation += 1

    def evoluerGarderParent(self, echant, mut_freq):
        """
        Fait evoluer la population courante en conservant les parents dans la selection
        """
        self.eval()
        tournoi = []
        nouvelle_pop = []
        #Prendre echant parents
        for i in range(echant):
            tournoi.append(self.selectionParRoulette())
        #Les croiser pour générer le même nombre d'enfants
        for i in range(echant):
            tournoi.append(tournoi[i].crossover(tournoi[i+1]))
        tournoi.append(tournoi[0].crossover(tournoi[1]))
        #Parmi cette selection, prendre les meilleurs
        tournoi.sort(key= lambda x: x.fitness())
        for i in range(echant):
            nouvelle_pop.append(tournoi[i])
        #Remplacement de la population
        self.individus = nouvelle_pop
        self.generation += 1


