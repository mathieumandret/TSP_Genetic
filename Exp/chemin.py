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

    def setListeVille(self, listeVilles):
        self.liste_villes = listeVilles

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
        

        

    def __repr__(self):
        return str(self.liste_villes)


            

