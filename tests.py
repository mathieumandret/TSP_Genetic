# coding: utf-8

import test_ville
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(test_ville('test_eq'))
