# -*- coding: utf-8 -*-
import random
import re
from collections import OrderedDict
from constants import *

class GeradorSentencas:
    MAXIMO_ITERACOES = 10000

    def __init__(self, gramatica):
        self.gramatica = gramatica
        self.conjunto_producoes = self.ordenar_conjunto_producoes(self.gramatica.conjunto_producoes)

    def gerar(self, sentenca = SIMBOLO_INICIAL):
        overflow = False
        historico = [sentenca]  
        i = 0

        while re.search('[A-Z]', sentenca):
            i += 1
            if i > self.MAXIMO_ITERACOES:
                overflow = True
                break

            for esquerda, direita in self.conjunto_producoes.iteritems():
                if esquerda in sentenca:
                    indice = random.randint(0, len(direita) - 1)
                    item_direita = direita[indice]
                    sentenca = sentenca.replace(esquerda, item_direita)
                    historico.append(sentenca)
                    break

        return (sentenca, historico, overflow)

    def ordenar_conjunto_producoes(self, conjunto_producoes):
        """
        Conjunto de produções é ordenado pelo tamanho da esquerda, decrescente,
        ou seja, os itens da esquerda com maior tamanho ficam em cima na lista.
        Exemplo:
        aA -> bA
        A -> c
        S -> aA|A
        Os maiores ficam acima para que eles tenham prioridade na substituição.
        """
        iteritems = conjunto_producoes.iteritems()
        return OrderedDict(sorted(iteritems, reverse = True, key = lambda x: len(x[0])))