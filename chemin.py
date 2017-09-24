from random import randint
from numpy.random import shuffle
from city import City
import copy


class Chemin:
    def __init__(self, length):
        self.liste_villes = []
        for i in range(length):
            self.liste_villes.append((City(randint(0, 100), randint(0, 100))))

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

    def __ne__(self, other):
        return (not self.__eq__(other))

    def crossover(self, other):
        """
        Croise le chemin courant avec un autre
        par PMX
        """

        def decouper(chemin, gauche, droite):
            print('decoupage')
            """
            Pour un chemin, retourne sa découpe
            selon 2 points
            """
            return chemin[gauche:droite], chemin[:gauche] + chemin[droite:]

        def recoller(inte, exte, gauche, droite):
            print('recollage')
            """
            Recolle une partie interieure et exterieure
            d'une decoupe selon gauche, droite
            """
            reco = []
            ii, ie = 0, 0
            for i in range(len(inte) + len(exte)):
                if i < gauche:
                    reco.append(exte[ie])
                    ie += 1
                elif i >= droite:
                    reco.append(exte[ie])
                    ie += 1
                else:
                    reco.append(inte[ii])
                    ii += 1
            return self.fromArray(reco)

        def reparer(inte, exte, echanges, gauche, droite):
            print('reparation')
            """
            Utilise le dictionnaire d'echanges pour eliminer
            les doublons d'un chemin
            """
            while (recoller(inte, exte, gauche, droite)).isLegal() == False:
                for i in range(len(exte)):
                    if exte[i] in inte:
                        exte[i] = echanges[exte[i]]

        def swap(chemin1, chemin2, gauche, droite):
            """
            Echange les parties entre gauche et droite des
            2 chemins
            """
            c1 = copy.deepcopy(chemin1)
            c2 = copy.deepcopy(chemin2)
            c1[gauche:droite], c2[gauche:droite] = c2[gauche:droite], c1[
                gauche:droite]
            return c1, c2

        #Selection aleatoire des points de decoupe
        gauche, droite = randint(0, len(self.liste_villes) - 1), randint(
            0, len(self.liste_villes))
        while droite <= gauche:
            droite = randint(0, len(self.liste_villes))
        #2 chemins apres l'echange
        A, B = swap(self.liste_villes, other.liste_villes, gauche, droite)
        # Parties interieures et exterieure de la decoupe
        inteA, exteA = decouper(A, gauche, droite)
        inteB, exteB = decouper(B, gauche, droite)
        #Dictionnaires qui contiendront la liste des echanges
        Aswaps, Bswaps = {}, {}
        #Pour chaque element de la partie interieure de A
        for i in range(len(inteA)): 
            #On ajoute au dictionnaire de B, l'element courant dans B 
            #comme cle, et celui de A comme valeur
            Bswaps[inteB[i]] = inteA[i]
        for i in range(len(inteB)): 
            Aswaps[inteA[i]] = inteB[i]
        #Avec ces dictionnaires, on peut reparer les chemins contenant des 
        #doublons
        reparer(inteA, exteA, Aswaps, gauche, droite)
        reparer(inteB, exteB, Bswaps, gauche, droite)
        #Recoller les parties
        return Chemin.fromArray(recoller(inteA, exteA, gauche, droite)), Chemin.fromArray(recoller(inteB, exteB, gauche, droite))
