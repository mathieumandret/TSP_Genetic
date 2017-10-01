#coding: utf-8

#Fonction pour calculer la distance etre 2 coordonnées
from math import hypot

class Ville:
    """
    Represente une ville par ses coordonnées x et y
    """

    def __init__(self, x, y):
        """
        Initialise une ville aux coordonnées x, y
        """
        self.x = x
        self.y = y

    def __repr__(self):
        """
        Retourne une représentation textuelle de la ville
        de la forme (x;y)
        """
        return "(" + str(self.x) + ";" + str(self.y) + ")"

    def distanceTo(self, other):
        """
        Retourne la distance entre cette ville et un autre
        """
        if not isinstance(other, Ville):
            raise ValueError('distanceTo doit prendre une ville en parametre')

        return hypot(other.x - self.x, other.y - self.y)

    def __eq__(self, other):
        """
        Permet de comparer 2 villes
        """
        if not isinstance(other, self.__class__):
            return False
        else:
            return self.x == other.x and self.y == other.y


    def __ne__(self, other):
        """
        Permet de comparer 2 villes
        """
        if not isinstance(other, self.__class__):
            return True
        else:
            return self.x != other.x or self.y != other.y

    def __hash__(self):
        """
        Hache la ville, permet de la stocker dans set()
        """
        #Hacher la représentation en string, qui contient x et y
        return hash(self.__repr__())
