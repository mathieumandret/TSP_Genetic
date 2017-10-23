# coding: utf-8

import unittest
from Ville import Ville


class TestVille(unittest.TestCase):

    def setUp(self):
        self.v = Ville(1, 2)

    def tearDown(self):
        self.v = None

    def test_repr(self):
        """
        Teste la representation textuelle d'une ville
        """
        self.assertEqual('(1;2)', self.v.__repr__())

    def test_distance_to(self):
        """
        Teste le calcul de distance entre 2 points
        """
        v2 = Ville(1, 3)
        self.assertEqual(self.v.distance_to(v2), 1)

    def test_eq(self):
        """
        Teste l'égalité entre 2 villes
        """
        v2 = Ville(1, 2)
        v3 = Ville(2, 1)
        self.assertEqual(self.v, v2)
        self.assertNotEqual(self.v, v3)

    def test_suite():
        suite = unittest.TestSuite()
        suite.addTest(TestVille('test_eq'))

if __name__ == '__main__':
    unittest.main()
