from constants import *

class GeradorFormalismoGramatica:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    @property
    def simbolos_nao_terminais(self):
        return self.__gerar_simbolos(self.gramatica.simbolos_nao_terminais)

    @property
    def simbolos_terminais(self):
        return self.__gerar_simbolos(self.gramatica.simbolos_terminais)

    @property
    def conjunto_producoes(self):
        linhas = []

        for esquerda, direita in self.gramatica.conjunto_producoes.iteritems():
            conjunto_producoes = self.adicionar_simbolo_sentenca_vazia(direita)
            linha = '%s -> %s' % (esquerda, '|'.join(conjunto_producoes))
            linhas.append(linha)

        return '{\n%s\n}' % self.__lista_para_string(linhas, 2)

    def adicionar_simbolo_sentenca_vazia(self, conjunto_producoes):
        conjunto_producoes = list(conjunto_producoes) # copia a lista

        for i, item in enumerate(conjunto_producoes):
            if item == '':
                conjunto_producoes[i] = SIMBOLO_SENTENCA_VAZIA

        return conjunto_producoes

    def gerar(self):
        str = 'G = (%s, %s, P, S)' % (self.simbolos_nao_terminais, self.simbolos_terminais)
        str += '\nP = %s' % self.conjunto_producoes
        return str

    def __lista_para_string(self, lista, nivel_identacao):
        identacao = nivel_identacao * ' '
        return '\n'.join([identacao + item for item in lista])

    def __gerar_simbolos(self, simbolos):
        return '{' + ', '.join(simbolos) + '}'