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

        while self.contem_nt(sentenca):
            i += 1
            if i > self.MAXIMO_ITERACOES:
                overflow = True
                break
            sentenca = self.gerar_derivacao(sentenca)
            historico.append(sentenca)

        return (sentenca, historico, overflow)

    def gerar_derivacao(self, sentenca):
        for esquerda, direita in self.conjunto_producoes.iteritems():
            if esquerda in sentenca:
                indice = random.choice(direita)
                sentenca = sentenca.replace(esquerda, item_direita)
                break
        return sentenca

    def contem_nt(self, sentenca):
        """Verifica se sentença contém símbolo não-terminal"""
        return bool(re.search('[A-Z]', sentenca))

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