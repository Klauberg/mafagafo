# -*- coding: utf-8 -*-
import unittest
from gramatica import *
from gramatica.arvore_derivacoes import *

class GeradorDerivacoesTest(unittest.TestCase):
    def test_gerar_derivacoes(self):
        gramatica = Gramatica(
            ['S', 'A', 'B'],
            ['a', 'b', 'c', 'd'],
            {
                'S': ['aBAa'],
                'A': ['b', 'cA'],
                'B': ['c', 'd']
            }
        )

        gd = GeradorDerivacoes(gramatica)
        derivacoes = gd.gerar_derivacoes('aBAa')
        self.assertEqual(derivacoes, ['acba', 'accAa', 'adba', 'adcAa'])