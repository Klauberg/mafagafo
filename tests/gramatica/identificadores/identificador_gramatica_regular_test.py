# -*- coding: utf-8 -*-

import unittest
from constants import *
from constants import SIMBOLO_INICIAL as S
from gramatica import *
from gramatica.identificadores import *

class IdentificadorGramaticaRegularTest(unittest.TestCase):
    def test_esquerda_com_apenas_um_nt(self):
        """
        Gramática com esquerda com apenas com 1 não-terminal deve ser reconhecida 
        como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a', 'aA'], 'A': ['a']}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_esquerda_com_mais_de_um_nt(self):
        """
        Gramática com esquerda com mais de 1 não-terminal não deve ser reconhecida 
        como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['A'+S, 'A'], 'A'+S: ['a'+S], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_esquerda_com_t(self):
        """
        Gramática com esquerda com não-terminal não deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['aS', 'A'], 'a'+S: ['aA'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A'], 'a': ['aA'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_um_t(self):
        """
        Gramática com um T na direita deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['aA'], 'A': ['a']}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_um_t_seguido_de_nt(self):
        """
        Gramática com um T seguido de NT na direita deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['aA'], 'A': ['aA', 'a']}
        )
        self.assertTrue(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_um_nt_seguido_de_t(self):
        """
        Gramática com um T seguido de NT na direita não deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['aA'], 'A': ['Aa', 'a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_mais_de_um_t(self):
        """
        Gramática com mais de um T seguido na direita não deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['aA'], 'A': ['aa', 'a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())

    def test_direita_com_apenas_um_nt(self):
        """
        Gramática com apenas um NT na direita não deve ser reconhecida como regular
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['A'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaRegular(gramatica).identificar())