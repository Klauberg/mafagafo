# -*- coding: utf-8 -*-

import unittest
from constants import *
from constants import SIMBOLO_INICIAL as S
from gramatica import *
from gramatica.identificadores import *

class IdentificadorGramaticaLivreDeContextoTest(unittest.TestCase):
    def test_esquerda_com_apenas_um_nt(self):
        """
        Gramática com esquerda com apenas com 1 não-terminal deve ser reconhecida 
        como livre de contexto
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a', 'aA'], 'A': ['a']}
        )
        self.assertTrue(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())

    def test_esquerda_com_mais_de_um_nt(self):
        """
        Gramática com esquerda com mais de 1 não-terminal não deve ser reconhecida 
        como livre de contexto
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['AS', 'A'], 'A'+S: ['a'+S], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())

    def test_esquerda_com_t(self):
        """
        Gramática com esquerda com não-terminal não deve ser reconhecida como livre
        de contexto
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A'], 'a'+S: ['aA'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())

        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A'], 'a': ['aA'], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())

    def test_direita_sem_sentenca_vazia(self):
        """
        Gramática com direita sem sentença vazia deve ser reconhecida como livre
        de contexto
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A', 'aa'], 'A': ['a']}
        )
        self.assertTrue(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())

    def test_direita_com_sentenca_vazia(self):
        """
        Gramática com direita com sentença vazia não deve ser reconhecida como livre
        de contexto
        """
        gramatica = Gramatica(
            [S, 'A'],
            ['a'],
            {S: ['a'+S, 'A', 'aa', ''], 'A': ['a']}
        )
        self.assertFalse(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())