import unittest
from gramatica import *
from constants import *
from constants import SIMBOLO_INICIAL as S
from constants import SIMBOLO_SENTENCA_VAZIA as X

class SelecionadorSentencaTesteGerarSemOverflow:
    i = 0
    def selecionar(self, sentencas):
        opcao = [0, 0, 1, 1, 0][self.i]
        self.i += 1
        return sentencas[opcao]

class SelecionadorSentencaTesteGerarComOverflow:
    def selecionar(self, sentencas):
        return sentencas[0]

class GeradorSentencasTest(unittest.TestCase):
    def test_gerar_sem_overflow(self):
        gramatica = Gramatica([S, 'A', 'B'], ['a', 'b'], {
            S: ['A', 'aA', 'Bb'],
            'A': ['aAb', 'B'],
            'aA': ['b', 'bB'],
            'B': ['', 'bB']
        })

        gerador = GeradorSentencas(gramatica, SelecionadorSentencaTesteGerarSemOverflow)
        output = gerador.gerar()

        self.assertEqual(output[0], 'bbb')
        self.assertEqual(output[1], ['S', 'A', 'aAb', 'bBb', 'bbBb', 'bbb'])
        self.assertFalse(output[2])

    def test_gerar_com_overflow(self):
        gramatica = Gramatica([S], ['a'], {
            S: [S, 'a']
        })

        gerador = GeradorSentencas(gramatica, SelecionadorSentencaTesteGerarComOverflow)
        output = gerador.gerar()

        self.assertTrue(output[2])