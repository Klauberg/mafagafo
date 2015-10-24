# -*- coding: utf-8 -*-
import unittest
from gramatica import *
from gramatica.gerador_formalismo_gramatica import *
from constants import SIMBOLO_SENTENCA_VAZIA as X

class GeradorFormalismoGramaticaTest(unittest.TestCase):
    def test_gerar_formalismo_com_sentenca_vazia(self):
        gramatica = Gramatica(
            ['S', 'A', 'B'],
            ['a', 'b', 'c'],
            {
                'S': ['AB', 'b'],
                'A': ['aAB', 'Aa', X],
                'B': ['b', 'bB']
            },
            'S'
        )

        str = 'G = ({S, A, B}, {a, b, c}, P, S)'
        str += '\nP = {\n'
        str += '  A -> aAB|Aa|%s\n' % X
        str += '  B -> b|bB\n'
        str += '  S -> AB|b\n'
        str += '}'

        gerador = GeradorFormalismoGramatica(gramatica)
        self.assertEqual(gerador.gerar(), str)

    def test_gerar_formalismo_sem_sentenca_vazia(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a', 'b', 'c'],
            {
                'S': ['aSc', 'A'],
                'A': ['b', 'bA']
            },
            'S'
        )

        str = 'G = ({S, A}, {a, b, c}, P, S)'
        str += '\nP = {\n'
        str += '  A -> b|bA\n'
        str += '  S -> aSc|A\n'
        str += '}'

        gerador = GeradorFormalismoGramatica(gramatica)
        self.assertEqual(gerador.gerar(), str)