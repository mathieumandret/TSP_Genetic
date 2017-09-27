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
        return hypot(other.x - self.x, other.y - self.y)
