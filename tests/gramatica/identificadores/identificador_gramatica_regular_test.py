# -*- coding: utf-8 -*-

import unittest
from gramatica import *
from gramatica.identificadores import *

class IdentificadorGramaticaRegularTest(unittest.TestCase):
    def test_esquerda_com_apenas_um_nt(self):
        """
        Gramática com esquerda com apenas com 1 não-terminal deve ser reconhecida 
        como regular
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['a', 'aA'], 'A': 'a'}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_esquerda_com_mais_de_um_nt(self):
        """
        Gramática com esquerda com mais de 1 não-terminal não deve ser reconhecida 
        como regular
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['AS', 'A'], 'AS': ['aS'], 'A': 'a'}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_esquerda_com_t(self):
        """
        Gramática com esquerda com não-terminal não deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aS', 'A'], 'aS': ['aA'], 'A': 'a'}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aS', 'A'], 'a': ['aA'], 'A': 'a'}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_um_t(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aA'], 'A': ['a']}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_um_t_seguido_de_nt(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aA'], 'A': ['aA', 'a']}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_mais_de_um_t(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aA'], 'A': ['aa', 'a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_apenas_um_nt(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['A'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())