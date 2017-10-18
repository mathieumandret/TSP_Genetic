# coding: utf-8

import unittest
import copy

from Ville import Ville
from Chemin import Chemin


class TestChemin(unittest.TestCase):
    def setUp(self):
        self.c = Chemin.from_array(
            [Ville(1, 2), Ville(1, 3),
             Ville(1, 4), Ville(1, 5)])

    def tearDown(self):
        self.c = None

    def test_from_array(self):
        l = [Ville(1, 2), Ville(1, 3), Ville(1, 4), Ville(1, 5)]
        ch = Chemin.from_array(l)
        self.assertEqual(ch.liste_villes, l)

    def test_repr(self):
        rep = '[(1;2), (1;3), (1;4), (1;5)]'
        self.assertEqual(self.c.__repr__(), rep)

    def test_len(self):
        self.assertEqual(self.c.__len__(), 4)

    def test_get_item(self):
        self.assertEqual(self.c[0], Ville(1, 2))

    def test_set_item(self):
        v = Ville(12, 12)
        self.c.__setitem__(0, v)
        self.assertEqual(self.c[0], v)

    def test_fitness(self):
        self.assertEqual(self.c.fitness(), 3)

    def test_to_plot(self):
        x = [1, 1, 1, 1]
        y = [2, 3, 4, 5]
        self.assertEqual(self.c.to_plot(), (x, y))

    def test_muter(self):
        copie = copy.deepcopy(self.c)
        self.assertNotEqual(self.c, copie)

if __name__ == '__main__':
    unittest.main()
