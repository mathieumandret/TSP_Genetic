from random import randint
from numpy.random import shuffle
from city import City
import copy

class Chemin:

    def __init__(self, length):
        #TODO garantir l'unicité
        self.liste_villes = []
        for i in range(length):
            self.liste_villes.append(City(randint(0,100), randint(0,100)))

    @classmethod
    def fromArray(self, array):
        """
        Constructeur alternatif, permet de
        creer un chemin en fournissant la liste de villes
        """
        c = Chemin(0)
        c.liste_villes = array
        return c

    def fitness(self):
        """
        Retourne la longueur du chemin
        """
        dist = 0
        for i in range(len(self.liste_villes)-1):
            dist += self.liste_villes[i].distanceTo(self.liste_villes[i+1])
        return dist
    
    def mutate(self):
        """
        Echange la postion de 2 villes dans le chemin
        """
        i = randint(0,len(self.liste_villes)-1)
        j = randint(0,len(self.liste_villes)-1)
        while i == j:
            j = randint(len(self.liste_villes)-1)
        self.liste_villes[i], self.liste_villes[j] = self.liste_villes[j], self.liste_villes[i] 

    def shuffle(self):
        """
        Renvoie une permutation du chemin
        """
        #On a besoin d'une copie profonde
        #si on utilise "=" on copie seulement 
        #la reference et tmp et self pointeront vers 
        #le meme objet
        tmp = copy.deepcopy(self)
        shuffle(tmp.liste_villes)
        return tmp

    def __len__(self):
        """
        Permet de retrouver le nombre de villes
        d'un chemin avec len(chemin)
        """
        return len(self.liste_villes)
        
    def __getitem__(self, key):
        """
        Permet d'acceder a une ville par
        Chemin[i]
        """
        return self.liste_villes[key]

    def __setitem__(self, key, item):
        """
        Permet de modifier une ville par
        Chemin[i] = ville
        """
        self.liste_villes[key] = item

    def estLegal(self):
        print(self.liste_villes)
        print(set(self.liste_villes))
        return len(self.liste_villes) == len(set(self.liste_villes))

    def __eq__(self, other):
        if isinstance(other, Chemin):
            return(self.liste_villes == other.liste_villes)
        else:
            return false

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return str(self.liste_villes)

    def __ne__(self, other):
        return (not self.__eq__(other))

    

            

