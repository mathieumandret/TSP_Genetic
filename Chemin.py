# coding: utf-8

from csv import reader
from Ville import Ville
from random import randint


class Chemin:
    """
    Represente un chemin, une liste ordonnée de villes
    """

    def __init__(self, nombre_villes):
        """
        Initialise un chemin de nombre_villes aléatoires

        """
        # Si on utilise ce constructeur depuis la methode de classe fromArray
        if nombre_villes == 0:
            # Ne pas creer de liste de villes
            pass
        self.liste_villes = set()
        while len(self.liste_villes) < nombre_villes:
            # Ajouter une ville aléatoires au chemin
            self.liste_villes.add(Ville(randint(0, 1000), randint(0, 1000)))
        self.liste_villes = list(self.liste_villes)
        if len(set(self.liste_villes)) != len(self.liste_villes):
            raise ValueError('NON UNIQUES')

    @classmethod
    def from_csv(cls, nom_fichier):
        """
        Permet la creation d'un chemin a partir d'un fichier csv
        contenant des coordonnées
        """
        coords = []
        with open(nom_fichier, 'r') as fichier:
            r = reader(fichier)
            for ligne in r:
                coords.append(Ville(float(ligne[0]), float(ligne[1])))
        c = Chemin(0)
        c.liste_villes = coords
        return c

    @classmethod
    def from_array(cls, liste_villes):
        """
        Permet la création d'un chemin à partir d'une liste de villes
        """
        # Ici on est sur que le tableau est valide
        # On cree un chemin vide
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
        # Il faut que les 2 parents soient de la même taille, et que other soit du type Chemin
        if not isinstance(other, self.__class__):
            raise ValueError('On ne peut croiser que 2 chemins')
        # Fils en forme canonique
        fils = [None] * len(self)
        # Selection aléatoire de 2 points points de découpe de 0 a longueur parent
        debut, fin = randint(0, len(self)), randint(0, len(self))

        # Si debut est strictement inférieur à fin, on peut traiter les fils
        # dans le sens normal
        if debut < fin:
            for i in range(debut, fin):
                # Le fils prends des élements du premier parent
                fils[i] = other[i]

        # Si le point de debut est plus grand que le point de fin, inverser
        elif debut > fin:
            for i in range(fin, debut):
                fils[i] = other[i]

        # Si les 2 points sont égaux(ce qui est peut probable pour un nombre de villes elevé, ne rien faire et laisser les fils tels quels
        # A ce point, il reste de "trous" (None) dans le fils, il faut les combler

        # Pour chaque element du parent
        for el in self:
            # Si l'element courant n'est pas déjà dans le fils
            if el not in fils:
                # On parcours toutes les cases du fils a la recherche du premier trou
                for j in range(len(fils)):
                    # Quand le trou est trouvé
                    if fils[j] is None:
                        # Il prends la valeur de l'element courant
                        fils[j] = el
                        # On n'a pas besoin de reparcourir le fils
                        break
        # On veut retourner 1 chemin:
        return Chemin.from_array(fils)

    def fitness(self):
        """
        Retourne la valeur de fitness de ce chemin, qui correspond a
        la distance totale entre ses villes
        """
        fitness = 0
        # Parcours de la premiere a l'avant derniere ville du chemin
        for i in range(len(self) - 1):
            # Ajouter la distance entre les 2 points courant a la distance totale
            fitness += self.liste_villes[i].distance_to(
                self.liste_villes[i + 1])
        return fitness

    def to_plot(self):
        """
        Retourne une liste de valeurs x et une liste de valeur y ordonnée,
        correspondant au chemin
        """
        x = []
        y = []
        for v in self.liste_villes:
            x.append(v.x)
            y.append(v.y)
        return x, y

    def muter_swap(self):
        """
        Echange aléatoirement la position de 2 villes dans le chemin
        """
        x, y = randint(0, len(self) - 1), randint(0, len(self) - 1)
        self[x], self[y] = self[y], self[x]

    def fermeture(self):
        """
        Retourne le chemin auquel est ajouté sa première
        ville en derniere position
        """
        return Chemin.from_array(self.liste_villes + self.liste_villes[:1])

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other is None:
            return False
        return self.liste_villes == other.liste_villes

    def __hash__(self):
        """
        Permet de hasher un objet chemin
        et donc de l'utiliser comme clé dans un
        dictionnaire
        """
        return hash(self.__repr__())
