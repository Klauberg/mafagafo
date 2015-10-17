# -*- coding: utf-8 -*-
import re
from constants import *
from collections import OrderedDict

class GeradorDerivacoes:
    def __init__(self, gramatica):
        self.gramatica = gramatica
        self.conjunto_producoes = self.__ordenar_conjunto_producoes()

    def gerar_derivacoes(self, sentenca):
        possiveis_substituicoes = self.__buscar_possiveis_substituicoes(sentenca)
        primeira_substituicao = self.__buscar_primeira_substituicao(possiveis_substituicoes)
        antes_simbolo_nt = sentenca[:primeira_substituicao[1]]
        depois_simbolo_nt = sentenca[(primeira_substituicao[1] + len(primeira_substituicao[0])):]
        prefixos = [antes_simbolo_nt + x for x in self.conjunto_producoes[primeira_substituicao[0]]]

        if self.contem_nt(depois_simbolo_nt):
            sufixos = self.gerar_derivacoes(depois_simbolo_nt)
        else:
            sufixos = [depois_simbolo_nt]

        return self.__combinar(prefixos, sufixos)

    def __buscar_primeira_substituicao(self, possiveis_substituicoes):
        return min(possiveis_substituicoes, key = lambda x: x[1])

    def __buscar_possiveis_substituicoes(self, sentenca):
        """
        Busca, para a sentença, possíveis símbolos NT a serem substituídos, juntamente
        com os índices onde se encontram
        """
        indices = [(esquerda, sentenca.find(esquerda))
                     for esquerda in self.conjunto_producoes]
        return filter(lambda x: x[1] != -1, indices)

    def __combinar(self, lista1, lista2):
        """
        Realiza combinação de itens de dois conjuntos (listas).
        Exemplo: lista1 = ['a', 'b'], lista2 = ['c', 'd']
        Resultado: ['ac', 'ad', 'bc', 'bd']
        """
        resultados = []
        for item1 in lista1:
            for item2 in lista2:
                resultados.append(item1 + item2)

        return resultados

    def __ordenar_conjunto_producoes(self):
        """
        Conjunto de produções é ordenado pelo tamanho da esquerda, decrescente,
        ou seja, os itens da esquerda com maior tamanho ficam em cima na lista.
        Exemplo:
        aA -> bA
        A -> c
        S -> aA|A
        Os maiores ficam acima para que eles tenham prioridade na substituição.
        """
        iteritems = self.gramatica.conjunto_producoes.iteritems()
        return OrderedDict(sorted(iteritems, reverse = True, key = lambda x: len(x[0])))

    # to-do: mover este método para outra classe utilitária, pois está repetido
    # em outras classes
    def contem_nt(self, x):
        """Verifica se a string contém símbolo não-terminal"""
        return bool(re.search('[A-Z]', x))