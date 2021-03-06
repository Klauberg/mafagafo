# -*- coding: utf-8 -*-
import unittest
from constants import *
from gramatica import *
from gramatica.identificadores import *

class IdentificadorGramaticaSensivelAoContextoTest(unittest.TestCase):
    def test_esquerda_menor_ou_igual_a_direita(self):
        """
        Gramática com esquerda menor ou igual à direita deve ser reconhecida como
        sensível ao contexto
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['a', 'aA'], 'A': ['a']},
            'S'
        )
        self.assertTrue(IdentificadorGramaticaSensivelAoContexto(gramatica).identificar())

    def test_esquerda_maior_que_direita(self):
        """
        Gramática com esquerda maior que direita não deve ser reconhecida como sensível
        ao contexto
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['AS', 'A'], 'AS': ['a', 'aa'], 'A': ['a']},
            'S'
        )
        self.assertFalse(IdentificadorGramaticaSensivelAoContexto(gramatica).identificar())

    def test_direita_com_sentenca_vazia(self):
        """
        Gramática com direita com sentença vazia não deve ser reconhecida como sensível
        ao contexto
        """
        gramatica = Gramatica(
            ['S', 'A'],
            ['a'],
            {'S': ['aS', 'A', 'aa', ''], 'A': ['a']},
            'S'
        )
        self.assertFalse(IdentificadorGramaticaLivreDeContexto(gramatica).identificar())