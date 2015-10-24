# -*- coding: utf-8 -*-
import unittest
from gramatica import *
from gramatica.arvore_derivacoes import *

class NoArvoreDerivacoesTest(unittest.TestCase):
    def test_nao_terminais_derivados(self):
        no1 = NoArvoreDerivacoes('S')

        no2 = NoArvoreDerivacoes('aBAa', no1)
        no1.nos.append(no2)
        self.assertEqual(no2.nao_terminais_derivados(), set(['S']))

        no3 = NoArvoreDerivacoes('acba', no2)
        no4 = NoArvoreDerivacoes('accAa', no2)
        no5 = NoArvoreDerivacoes('adba', no2)
        no6 = NoArvoreDerivacoes('adcAa', no2)
        no2.nos.extend([no3, no4, no5, no6])

        for no in no2.nos:
            self.assertEqual(no.nao_terminais_derivados(), set(['S', 'A', 'B']))

    def test_contem_recursao(self):
        no1 = NoArvoreDerivacoes('S')

        no2 = NoArvoreDerivacoes('aBAa', no1)
        no1.nos.append(no2)
        self.assertFalse(no2.contem_recursao())

        no3 = NoArvoreDerivacoes('accAa', no2)
        no2.nos.append(no3)
        self.assertTrue(no3.contem_recursao())

    def test_quantidade_derivacoes(self):
        no1 = NoArvoreDerivacoes('S')
        self.assertEqual(no1.quantidade_derivacoes(), 0)

        no2 = NoArvoreDerivacoes('A', no1)
        no1.nos.append(no2)
        self.assertEqual(no2.quantidade_derivacoes(), 1)

        no3 = NoArvoreDerivacoes('B', no2)
        no2.nos.append(no3)
        self.assertEqual(no3.quantidade_derivacoes(), 2)

        no4 = NoArvoreDerivacoes('C', no3)
        no3.nos.append(no4)
        self.assertEqual(no4.quantidade_derivacoes(), 3)

        no5 = NoArvoreDerivacoes('a', no4)
        no4.nos.append(no5)
        self.assertEqual(no5.quantidade_derivacoes(), 4)