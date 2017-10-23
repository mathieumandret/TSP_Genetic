# coding: utf-8

import unittest
from Population import Population
from Chemin import Chemin


class TestVille(unittest.TestCase):
    def setUp(self):
        # On cree une population de toutes les permutations possibles
        self.p = Population.gen_deter(Chemin.from_csv("coords.csv"))

    def tearDown(self):
        self.p = None

    def test_len(self):
        self.assertEqual(len(self.p.individus), 120)

    def test_eval(self):
        self.p.eval()
        meilleur = Chemin.from_array(

    def test_trier_meilleurs(self):
        self.p.trier_meilleurs()
        self.assertTrue(self.p.individus[0].fermeture().fitness() <
                   self.p.individus[1].fermeture().fitness())

if __name__ == '__main__':
    unittest.main()
