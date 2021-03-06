# -*- coding: utf-8 -*-
import unittest
from gramatica import *
from constants import *

class GramaticaTest(unittest.TestCase):
    NAO_TERMINAIS = ['S', 'A']
    TERMINAIS = ['a', 'b']
    SIMBOLO_INICIAL = 'S'
    CONJUNTO_PRODUCOES = {
        'S': ['aA', 'a'],
        'A': ['b', 'A']
    }

    def setUp(self):
        self.gramatica = Gramatica(self.NAO_TERMINAIS, self.TERMINAIS,
            self.CONJUNTO_PRODUCOES, self.SIMBOLO_INICIAL)

    def test_simbolos_nao_terminais(self):
        self.assertEqual(self.gramatica.simbolos_nao_terminais, self.NAO_TERMINAIS)

    def test_simbolos_terminais(self):
        self.assertEqual(self.gramatica.simbolos_terminais, self.TERMINAIS)

    def test_simbolos_conjunto_producoes(self):
        self.assertEqual(self.gramatica.conjunto_producoes, self.CONJUNTO_PRODUCOES)

    def test_simbolo_inicial(self):
        self.assertEqual(self.gramatica.simbolo_inicial, self.SIMBOLO_INICIAL)