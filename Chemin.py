#coding: utf-8


from Ville import Ville
from random import randint
import pdb

class Chemin:
    """
    Represente un chemin, une liste ordonnée de villes
    """

    def __init__(self, nombre_villes):
        """
        Initialise un chemin de nombre_villes aléatoires

        """
        if nombre_villes == 0:
            pass
        #TODO Probleme: une ville peut apparaitre plusieurs fois dans le chemin, causant des trous dans les fils par crossover !!!
        #Liste qui contiendra toutes les villes du chemin
        self.liste_villes = set()
        while len(self.liste_villes) < nombre_villes:
            #Ajouter une ville aléatoires au chemin
            self.liste_villes.add(Ville(randint(0,500), randint(0,500)))
        self.liste_villes = list(self.liste_villes)
        if len(set(self.liste_villes)) != len(self.liste_villes):
            raise ValueError('NON UNIQUES')

    @classmethod
    def fromArray(self, liste_villes):
        """
        Permet la création d'un chemin à partir d'une liste de villes
        """
        #Ici on est sur que le tableau est valide
        #On cree un chemin vide 
        c = Chemin(0)
        c.liste_villes = liste_villes
        return c

    def __repr__(self):
        """
        Donne une représentation textuelle du chemin de la forme
        [(x;y), (x;y) ...]
        """
        return str(self.liste_villes)

    def __len__(self):
        """
        Permet d'utiliser len() sur un Chemin pour éviter
        d'avoir a fair len(self.liste_villes) quand on veut le nombre
        de villes dans le chemin
        """
        return len(self.liste_villes)
    
    def __getitem__(self, pos):
        """
        Permet l'indexation: Chemin[pos]
        """
        return self.liste_villes[pos]
    
    def __setitem__(self, key, item):
        """
        Permet la modification 
        avec Chemin[key] = item 
        """
        self.liste_villes[key] = item 

    def crossover(self, other):
        """
        Croise le chemin courant et un autre pour retourner 2 chemins fils
        """
        #Il faut que les 2 parents soient de la même taille, et que other soit du type Chemin
        #Fils en forme canonique
        fils =[Ville(-1,-1)] * len(self)
        fils = Chemin.fromArray(fils)
        #Selection aléatoire de 2 points points de découpe de 0 a longueur parent
        debut, fin = randint(0,len(self)), randint(0, len(self))
        
        #Si debut est strictement inférieur à fin, on peut traiter les fils 
        #dans le sens normal
        if debut < fin:
            for i in range(debut, fin):
                #Le fils prends des élements du premier parent
                fils[i] = other.liste_villes[i]

        #Si le point de debut est plus grand que le point de fin, inverser
        elif debut > fin:
            for i in range(fin, debut):
                fils[i] = other.liste_villes[i]


        #Si les 2 points sont égaux(ce qui est peut probable pour un nombre de villes elevé, ne rien faire et laisser les fils tels quels
        #A ce point, il reste de "trous" (None) dans le fils, il faut les combler
        ref = Ville(-1, -1)
        #Des Nones restent à la fin pour une liste_villes très grande
        for el in self.liste_villes:
            if el not in fils:
                for j in range(len(fils)):
                    if fils[j] == ref :
                        fils[j] = el
                        break
        #On veut retourner 1 chemin:
        return fils

    def fitness(self):
        """
        Retourne la valeur de fitness de ce chemin, qui correspond a 
        la distance totale entre ses villes
        """
        fitness = 0
        #Parcours de la premiere a l'avant derniere ville du chemin
        for i in range(len(self)-1):
            #Ajouter la distance entre les 2 points courant a la distance totale
            fitness += self.liste_villes[i].distanceTo(self.liste_villes[i+1])
        return fitness

    def muter(self):
        """
        Echange aléatoirement la position de 2 villes dans le chemin
        """
        x, y = randint(0, len(self)-1), randint(0, len(self)-1)
        self.liste_villes[x], self.liste_villes[y] = self.liste_villes[y], self.liste_villes[x]



