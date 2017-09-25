from random import randint
from numpy.random import shuffle
from city import City
import copy


class Chemin:
    def __init__(self, length, array=None):
        if array == None:
            self.liste_villes = []
            for i in range(length):
                self.liste_villes.append((City(randint(0, 100), randint(0, 100)))) 
        else:
            self.liste_villes = array

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
        for i in range(len(self.liste_villes) - 1):
            dist += self.liste_villes[i].distanceTo(self.liste_villes[i + 1])
        return dist

    def betterCrossover(self, other):
        #Forme cannonique
        child1 = [None] * len(self)
        child2 = [None] * len(self)
        debut, fin = randint(0, len(self)), randint(0, len(self))

        if  debut < fin: 
            #Copier le contenu de l'intervalle depuis le parent1
            for i in range(debut, fin):
                child1[i] = self[i]
                child2[i] = other[i]
        elif debut >= fin:
            for i in range(fin, debut):
                child1[i] = self[i]
                child2[i] = other[i]

        #Selon les points debut, fin, il reste des None dans les 2 enfants

        #Pour chaque element du second parent
        for i in range(len(other)):
            #Si l'element du parent n'est pas déjà dans l'enfant
            if other[i] not in child1:
                #Rechercher la prochaine cellule a None de l'enfant
                for j in range(len(child1)):
                    #Si la cellule courante est un None
                    if child1[j] == None:
                        #Placer l'element i du parent a cet endroit
                        child1[j] = other[i]
                        #Sortir du for parcourant tout les elements de l'enfant
                        break


        for k in range(len(self)):
            #Si la ville courante n'est pas dans l'enfant
            if not self[k] in child2:
                #Rechercher la premiere cellule vide
                for l in range(len(child2)):
                    if child2[l] == None:
                        child2[l] = self[k]
                        break
        return Chemin(0, child1), Chemin(0, child2)

    def mutate(self):
        """
        Echange la postion de 2 villes dans le chemin
        """
        i = randint(0, len(self.liste_villes) - 1)
        j = randint(0, len(self.liste_villes) - 1)
        while i == j:
            j = randint(0, len(self.liste_villes) - 1)
        self.liste_villes[i], self.liste_villes[j] = self.liste_villes[
            j], self.liste_villes[i]

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

    def isLegal(self):
        return len(self.liste_villes) == len(set(self.liste_villes))

    def __eq__(self, other):
        if isinstance(other, Chemin):
            return (self.liste_villes == other.liste_villes)
        else:
            return False

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return str(self.liste_villes)
