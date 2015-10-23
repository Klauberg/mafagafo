# -*- coding: utf-8 -*-

import unittest
from constants import *
from constants import SIMBOLO_INICIAL as S
from gramatica import *
from gramatica.identificadores import *

class IdentificadorGramaticaIrrestritaTest(unittest.TestCase):
    def test_esquerda_com_nt(self):
        """Gramática com esquerda tendo NT deve ser considerada irrestrita"""
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a', 'aA'], 'A': ['a']},
            S
        )
        self.assertTrue(IdentificadorGramaticaIrrestrita(gramatica).identificar())

    def test_esquerda_com_mais_de_um_nt(self):
        """Gramática com esquerda não tendo NT não deve ser considerada irrestrita"""
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['A'+S, 'A'], 'a': ['a']},
            S
        )
        self.assertFalse(IdentificadorGramaticaIrrestrita(gramatica).identificar())

    def test_direita_sem_sentenca_vazia(self):
        """Gramática com direita sem sentença vazia deve ser reconhecida como irrestrita"""
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A', 'aa'], 'A': ['a']},
            S
        )
        self.assertTrue(IdentificadorGramaticaIrrestrita(gramatica).identificar())

    def test_direita_com_sentenca_vazia(self):
        """Gramática com direita com sentença vazia deve ser reconhecida como irrestrita"""
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A', 'aa', ''], 'A': ['a']},
            S
        )
        self.assertTrue(IdentificadorGramaticaIrrestrita(gramatica).identificar())