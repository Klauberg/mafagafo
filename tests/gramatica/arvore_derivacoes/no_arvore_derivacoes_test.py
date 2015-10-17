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


