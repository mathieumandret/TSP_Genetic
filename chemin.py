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
        elif debut > fin:
            for i in range(fin, debut):
                child1[i] = self[i]
                child2[i] = other[i]

        #Parcours du deuxieme parent
        for i in range(len(other)):
            #Si la ville courante n'est pas dans l'enfant
            if other[i] not in child1:
                #Rechercher la premiere cellule vide
                for j in range(len(child1)):
                    if child1[j] == None:
                        child1[j] = other[j]
                        break

        for i in range(len(self)):
            #Si la ville courante n'est pas dans l'enfant
            if self[i] not in child2:
                #Rechercher la premiere cellule vide
                for j in range(len(child2)):
                    if child2[j] == None:
                        child2[j] = self[j]
                        break

        return Chemin.fromArray(child1), Chemin.fromArray(child2)

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
            avant = chemin[:gauche]
            milieu = chemin[gauche:droite]
            apres = chemin[droite:]
            return avant, milieu, apres

        def recoller(avant, milieu, apres, gauche, droite):
            print('recollage')
            """
            Recolle une partie interieure et exterieure
            d'une decoupe selon gauche, droite
            """
            reco = avant + milieu + apres
            print('fait')
            return self.fromArray(reco)

        def reparer(avant, milieu, apres, echanges, gauche, droite):
            print('reparation')
            """
            Utilise le dictionnaire d'echanges pour eliminer
            les doublons d'un chemin
            """
            rep = recoller(avant, milieu, apres, gauche, droite)
            while rep.isLegal() == False:
                for i in range(len(avant)):
                    if avant[i] in milieu:
                        print(avant[i])
                        avant[i] = echanges[avant[i]]
                for i in range(len(apres)):
                    if apres[i] in milieu:
                        apres[i] = echanges[apres[i]]
                rep = recoller(avant, milieu, apres, gauche, droite)
            return rep

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
        avantA, milieuA, exteA = decouper(A, gauche, droite)
        avantB, milieuB, exteB = decouper(B, gauche, droite)
        #Dictionnaires qui contiendront la liste des echanges
        Aswaps, Bswaps = {}, {}
        #Pour chaque element de la partie interieure de A
        for i in range(len(milieuA)):
            #On ajoute au dictionnaire de B, l'element courant dans B
            #comme cle, et celui de A comme valeur
            Bswaps[milieuB[i]] = milieuA[i]
        for i in range(len(milieuB)):
            Aswaps[milieuA[i]] = milieuB[i]
        #Avec ces dictionnaires, on peut reparer les chemins contenant des
        #doublons
        return Chemin.fromArray(
            reparer(avantA, milieuA, exteA, Aswaps, gauche, droite)
        ), Chemin.fromArray(
            reparer(avantB, milieuB, exteB, Bswaps, gauche, droite))
