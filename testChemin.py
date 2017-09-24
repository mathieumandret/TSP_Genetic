#coding: utf-8

import unittest
from chemin import Chemin
from city import City
from copy import deepcopy

class TestChemin(unittest.TestCase):
   
    def test_fromArray(self):
        c = Chemin.fromArray([1,2,3,4])
        self.assertEqual(c.liste_villes, [1,2,3,4])

    def test_Fitness(self):
        c = Chemin.fromArray([City(0,1), City(2,3)])
        self.assertEqual(c.fitness(),2.8284271247461903) 

    def test_Mutate(self):
        c = Chemin(4)
        c2 = deepcopy(c)
        c.mutate()
        self.assertNotEqual(c,c2)

    def test_shuffle(self):
        c = Chemin(4)
        self.assertNotEqual(c, c.shuffle())

    def test__len(self):
        c = Chemin(4)
        self.assertEqual(len(c), 4)


    def test_isLegal(self):
       c = Chemin.fromArray([City(0,1), City(0,1)]) 
       self.assertFalse(c.isLegal())
        
    def test_decouper_recoller(self):
        j = Chemin(4)
        k = Chemin(4)
        self.assertEqual(j.crossover(k),j)


unittest.main()
