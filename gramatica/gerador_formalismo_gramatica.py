# -*- coding: utf-8 -*-
from constants import *
from collections import OrderedDict

class GeradorFormalismoGramatica:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def gerar_simbolos_nao_terminais(self):
        return self.__gerar_simbolos(self.gramatica.simbolos_nao_terminais)

    def gerar_simbolos_terminais(self):
        return self.__gerar_simbolos(self.gramatica.simbolos_terminais)

    def gerar_conjunto_producoes(self):
        linhas = []
        ordenado = self.__conjunto_producoes_ordenado()

        for esquerda, direita in ordenado.iteritems():
            # A sentença vazia é representada como uma string vazia na estrutura da
            # classe Gramatica, mas queremos exibir o símbolo que representa a
            # sentença vazia quando geramos a string do formalismo da gramática
            conjunto_producoes = self.adicionar_simbolo_sentenca_vazia(direita)

            linha = '%s -> %s' % (esquerda, '|'.join(conjunto_producoes))
            linhas.append(linha)

        return '{\n%s\n}' % self.__lista_para_string(linhas, 2)

    def adicionar_simbolo_sentenca_vazia(self, conjunto_producoes):
        """
        Substitui strings vazias do conjunto de produções pelo símbolo de sentença
        vazia
        """
        conjunto_producoes = list(conjunto_producoes) # copia a lista

        for i, item in enumerate(conjunto_producoes):
            if item == '':
                conjunto_producoes[i] = SIMBOLO_SENTENCA_VAZIA

        return conjunto_producoes

    def gerar(self):
        str = 'G = (%s, %s, P, %s)' % (self.gerar_simbolos_nao_terminais(),
            self.gerar_simbolos_terminais(), self.gramatica.simbolo_inicial)
        str += '\nP = %s' % self.gerar_conjunto_producoes()
        return str

    def __lista_para_string(self, lista, nivel_identacao):
        identacao = nivel_identacao * ' '
        return '\n'.join([identacao + item for item in lista])

    def __gerar_simbolos(self, simbolos):
        return '{' + ', '.join(simbolos) + '}'

    def __conjunto_producoes_ordenado(self):
        return OrderedDict(sorted(self.gramatica.conjunto_producoes.items()))