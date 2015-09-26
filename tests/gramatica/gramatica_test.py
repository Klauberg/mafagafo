import unittest
from gramatica import *

class GramaticaTest(unittest.TestCase):
    NAO_TERMINAIS = ['S', 'A']
    TERMINAIS = ['a', 'b']
    CONJUNTO_PRODUCOES = {
        'S': ['aA', 'a'],
        'A': ['b', 'A']
    }

    def setUp(self):
        self.gramatica = Gramatica(self.NAO_TERMINAIS, self.TERMINAIS, self.CONJUNTO_PRODUCOES)

    def test_simbolos_nao_terminais(self):
        self.assertEqual(self.gramatica.simbolos_nao_terminais, self.NAO_TERMINAIS)

    def test_simbolos_terminais(self):
        self.assertEqual(self.gramatica.simbolos_terminais, self.TERMINAIS)

    def test_simbolos_conjunto_producoes(self):
        self.assertEqual(self.gramatica.conjunto_producoes, self.CONJUNTO_PRODUCOES)