#coding: utf-8

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
        #Liste qui contiendra toutes les villes du chemin
        self.liste_villes = []
        for i in range(nombre_villes):
            #Ajouter une ville aléatoires au chemin
            self.liste_villes.append(Ville(randint(0,100), randint(0,100)))

    @classmethod
    def fromArray(self, liste_villes):
        """
        Permet la création d'un chemin à partir d'une liste de villes
        """
        #Il faut que la liste passée en parametre soit une liste de Villes
        #et qu'elle contiennent au moins un element
        if len(liste_villes) == 0 or not isinstance(liste_villes[0], Ville):
            #TODO définir une exception personnalisée
            raise ValueError('Il faut passer un tableau d\' au moins 1 tuple a la methode fromArray de Chemin')
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

    def crossover(self, other):
        """
        Croise le chemin courant et un autre pour retourner 2 chemins fils
        """
        #Il faut que les 2 parents soient de la même taille, et que other soit du type Chemin
        if not isinstance(other,Chemin) or len(self)!=len(other):
            raise ValueError('Un crossover doit etre fait entre 2 chemins de longueur egale')
        #Fils en forme canonique
        premier_fils = [None] * len(self)
        second_fils = [None] * len(self)

        #Selection aléatoire de 2 points points de découpe de 0 a longueur parent
        debut, fin = randint(0,len(self)), randint(0, len(self))
        
        #Si debut est strictement inférieur à fin, on peut traiter les fils 
        #dans le sens normal
        if debut < fin:
            for i in range(debut, fin):
                #Le premier fils prends des élements du premier parent
                premier_fils[i] = self.liste_villes[i]
                #Le second fils prends des élements du deuxième parent
                second_fils[i] = other.liste_villes[i]

        #Si le point de debut est plus grand que le point de fin, inverser
        elif debut > fin:
            for i in range(fin, debut):
                premier_fils[i] = self.liste_villes[i]
                second_fils[i] = other.liste_villes[i]

        #Si les 2 points sont égaux(ce qui est peut probable pour un nombre de villes elevé, ne rien faire et laisser les fils tels quels
        #A ce point, il reste de "trous" (None) dans les fils, il faut les combler

        #Pour chaque element du premier parent
        for i in range(len(self)):
            #On verifie que l'element courant du parent ne soit pas déjà présent dans le second fils
            if self.liste_villes[i] not in second_fils:
                #Chercher le premier trou dans le fils
                for j in range(len(second_fils)):
                    if second_fils[j] == None:
                        #On a trouvé un trou, y placer l'élément courant du parent
                        second_fils[j] = self.liste_villes[i]
            #Utiliser la meme boucle pour le premier_fils
            if other.liste_villes[i] not in premier_fils:
                for j in range(len(premier_fils)):
                    if premier_fils[j] == None:
                        premier_fils[j] = other.liste_villes[i]

        #On veut retourner 2 chemins:
        return Chemin.fromArray(premier_fils), Chemin.fromArray(second_fils)

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



