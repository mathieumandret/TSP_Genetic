# coding: utf-8

from Chemin import Chemin
from random import sample, randint, uniform, shuffle
from math import inf
from itertools import permutations


class Population:
    """
    Represente une population de n chemins, tous composés des memes villes
    """

    def __init__(self, nb_individus, nb_villes, csv=None):
        """
        Initialise une population de nbIndividus, chemins reliant nbVilles
        """
        # Permet de suivre l'évolution
        self.generation = 1
        self.individus = []
        # Pour recuperer la meilleure fitness, on doit être sur
        # que le premiere valeur qu'on evalueara sera inférieure
        # a meilleurFitness
        self.meilleurFitness = inf
        # Dictionnaire qui à chaque chemin associe sa longueur
        self.cache = {}
        # Membre de la population de distance la plus courte, inexistant a
        # l'initilisation
        self.meilleurChemin = None
        # Permet de creer une population vide
        if nb_individus == 0:
            return
        # generation de la population
        if csv is not None:
            carte = Chemin.from_csv(csv)
        else:
            # Creation de la carte, qui est un chemin dont l'ordre n'importe
            # pas, il sert de base a la
            carte = Chemin(nb_villes)
        # Melanger la carte
        shuffle(carte)
        self.individus.append(carte)
        # Tant qu'on a pas atteint le nombre d'individus cible
        while len(self.individus) < nb_individus:
            # On choisit une permutation aléatoire de la carte
            perm = Chemin.from_array(sample(carte.liste_villes, len(carte)))
            # Si elle n'est pas déjà présente dans la population
            # on l'y ajoute.
            if perm not in self.individus:
                self.individus.append(perm)
        # Evaluation de la population
        self.eval()

    def __repr__(self):
        """
        Retourne une représentation textuelle de la population
        """
        rep = ""
        for chemin in self.individus:
            rep += chemin.__repr__() + '\n'
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
        for chemin in self.individus:
            # Si le chemin existe dans le cache,
            # on connait déjà sa longueur
            if chemin in self.cache.keys():
                fit = self.cache[chemin]
            else:
                # Sinon on doit la calculer
                fit = chemin.fermeture().fitness()
                # Et le mettre dans le cache
                self.cache[chemin] = fit
            if fit < self.meilleurFitness:
                self.meilleurChemin = chemin.fermeture()
                self.meilleurFitness = fit

    def trier_meilleurs(self):
        """
        Trie la population en plaçant les chemins les plus courts en premier
        """
        # Tri avec pour cle la fonction fitness de Chemin
        self.individus.sort(key=lambda x: x.fitness())

    def selection_par_roulette(self):
        """
        Utilise la selection par roulette pour generer n nouveau individus
        """
        # Calcul de la fitness total
        total = 0
        i = 0
        for chemin in self.individus:
            total += chemin.fitness()
        r = uniform(0, total)
        while (r > 0):
            r -= self.individus[i].fitness()
            i += 1
        return self.individus[i - 1]

    def selection_par_tournoi(self, n):
        """
        A partir d'un echantillon aléatoire de n individus,
        selectionne le meilleur
        """
        # Selection de n membre de la population
        participants = sample(self.individus, n)
        # Recherche du meilleur participant
        participants.sort(key=lambda x: x.fitness())
        # Selection du meilleur participant, qui a donc la plus petite valeur
        # de fitness
        return participants[0]

    def evoluer(self, mut_freq, methode_select,
                methode_mut, elit, pourcent_parent=0):
        """
        Fait evoluer la population avec une methode
        de selection, de mutation et des paramètres
        donnés
        """
        # tableau qui contiendra les fils de individus
        nouvelle_pop = []
        # Si on doit garder des parents, les selectionner
        if elit:
            self.individus.sort(key=lambda x: x.fitness())
            nb_parents = int(len(self.individus) * (pourcent_parent / 100))
            nouvelle_pop += self.individus[:nb_parents]
        # Pour chaque element de la population parente
        for i in range(len(self.individus)):
            # Choisir 2 parents selon la methode de selection passée en
            # paramètres.
            p1 = self.selection_par_roulette(
            ) if methode_select == 'roulette' else self.selection_par_tournoi(int(len(self) * 0.2))
            p2 = self.selection_par_roulette(
            ) if methode_select == 'roulette' else self.selection_par_tournoi(int(len(self) * 0.2))
            fils = p1.crossover(p2)
            self.pot_mut(fils, methode_mut, mut_freq)
            nouvelle_pop.append(fils)
            # Remplacer l'ancienne population par la nouvelle
        self.individus = nouvelle_pop
        self.eval()
        self.generation += 1

    def pot_mut(self, fils, methode, mut_freq):
        r = randint(0, 100)
        if mut_freq > r:
            if methode == 'swap':
                fils.muter_swap()
            elif methode == 'scramble':
                fils.muter_scramb()

    @classmethod
    def gen_deter(cls, carte):
        """
        Cette méthode ne doit être utilisée qu'a but de test
        Elle permet de generer toutes les permutations possibles
        depuis un chemin
        """
        # Population vide
        p = Population(0, 0)
        carte = Chemin.from_csv("test_coords.csv")
        # Liste de toutes les permutations de la carte
        for perm in permutations(carte):
            p.individus.append(Chemin.from_array(list(perm)))
        p.eval()
        return p
