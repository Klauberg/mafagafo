# -*- coding: utf-8 -*-
import unittest
from gramatica import *
from gramatica.arvore_derivacoes import *

class ArvoreDerivacoesTest(unittest.TestCase):
    def test_gerar_novo_nivel(self):
        gramatica = Gramatica(
            ['S', 'A', 'B'],
            ['a', 'b', 'c', 'd'],
            {
                'S': ['aBAa'],
                'A': ['b', 'cA'],
                'B': ['c', 'd']
            },
            'S'
        )

        arvore = ArvoreDerivacoes(gramatica)
        self.assertEqual(len(arvore.folhas), 1)
        self.assertEqual(arvore.folhas[0].sentenca, 'S')

        progresso = arvore.gerar_novo_nivel(True)
        self.assertTrue(progresso)
        self.assertEqual(len(arvore.folhas), 1)
        self.assertEqual(arvore.folhas[0].sentenca, 'aBAa')

        progresso = arvore.gerar_novo_nivel(True)
        self.assertTrue(progresso)
        self.assertEqual(set([no.sentenca for no in arvore.folhas]),
            set(['acba', 'accAa', 'adba', 'adcAa']))

        # não deve haver progresso pois encontrou recursão, e estamos passando
        # parâmetro para impedir recursão
        progresso = arvore.gerar_novo_nivel(True)
        self.assertFalse(progresso)

        # deve haver progresso pois não estamos impedindo recursão nessa chamada
        progresso = arvore.gerar_novo_nivel(False)
        self.assertTrue(progresso)
        self.assertEqual(set([no.sentenca for no in arvore.folhas]),
            set(['acba', 'accba', 'acccAa', 'adba', 'adcba', 'adccAa']))

    def test_montar_sem_recursao(self):
        gramatica = Gramatica(
            ['S', 'A', 'B'],
            ['a', 'b', 'c', 'd'],
            {
                'S': ['aBAa'],
                'A': ['b', 'cA'],
                'B': ['c', 'd']
            },
            'S'
        )

        arvore = ArvoreDerivacoes(gramatica).montar_sem_recursao()
        self.assertEqual(set([no.sentenca for no in arvore.folhas]),
            set(['acba', 'accAa', 'adba', 'adcAa']))

    def test_buscar_sentencas_finais(self):
        gramatica = Gramatica(
            ['S', 'A', 'B'],
            ['a', 'b', 'c', 'd'],
            {
                'S': ['aBAa'],
                'A': ['b', 'cA'],
                'B': ['c', 'd']
            },
            'S'
        )

        arvore = ArvoreDerivacoes(gramatica).montar_sem_recursao()
        self.assertEqual(set(arvore.buscar_sentencas_finais()),
            set(['acba', 'adba']))

    def test_buscar_sentencas_minimas(self):
        gramatica = Gramatica(
            ['S', 'A'],
            ['a', 'b'],
            {
                'S': ['a', 'bA'],
                'A': ['', 'a']
            },
            'S'
        )

        arvore = ArvoreDerivacoes(gramatica).montar_sem_recursao()
        self.assertEqual(set(arvore.buscar_sentencas_minimas()), set(['a', 'b']))

    def test_pode_gerar_sentenca_finita(self):
        gramatica = Gramatica(['S'], ['a'], {'S': ['aS']}, 'S')
        arvore = ArvoreDerivacoes(gramatica).montar_sem_recursao()
        self.assertFalse(arvore.pode_gerar_sentenca_finita())

        gramatica = Gramatica(['S'], ['a'], {'S': ['aS', 'b']}, 'S')
        arvore = ArvoreDerivacoes(gramatica).montar_sem_recursao()
        self.assertTrue(arvore.pode_gerar_sentenca_finita())