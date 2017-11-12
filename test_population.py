# coding: utf-8

import unittest
from Population import Population
from Chemin import Chemin
from Ville import Ville


class TestPopulation(unittest.TestCase):
    def setUp(self):
        # On cree une population de toutes les permutations possibles
        self.p = Population.gen_deter("test_coords.csv")

    def tearDown(self):
        self.p = None

    def test_len(self):
        self.assertEqual(len(self.p.individus), 120)

    def test_meilleur_chemin(self):
        # Meilleur chemin connu grace a l'algorithme deterministe
        meilleur = Chemin.from_array([
            Ville(405, 122),
            Ville(404, 207),
            Ville(286, 196),
            Ville(35, 90),
            Ville(132, 98),
            Ville(405, 122)
        ])
        # Meilleur chemin calcule
        meilleur_c = self.p.meilleurChemin
        self.assertEqual(meilleur, meilleur_c)

    def test_meilleur_score(self):
        cible = 847.3644139827088
        self.assertEqual(self.p.meilleurFitness, cible)

    def test_trier_meilleurs(self):
        self.p.trier_meilleurs()
        self.assertTrue(self.p.individus[0].fermeture().fitness() <
                        self.p.individus[1].fermeture().fitness())

    def test_eval(self):
        self.p.eval()
        self.assertTrue(self.p.meilleurChemin is not None)
        self.assertEqual(len(self.p.meilleurChemin), 6)

    def test_evoluer_roulette(self):
        pop = Population(10, 30)
        pop.eval()
        ancient_score = pop.meilleurFitness
        pop.evoluer_roulette(30)
        pop.eval()
        self.assertTrue(ancient_score >= pop.meilleurFitness)

    def test_evoluer_tournoi(self):
        pop = Population(10, 30)
        pop.eval()
        ancient_score = pop.meilleurFitness
        pop.evoluer_tournoi(30)
        pop.eval()
        self.assertTrue(ancient_score >= pop.meilleurFitness)


if __name__ == '__main__':
    unittest.main()
