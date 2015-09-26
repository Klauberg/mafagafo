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

        for nao_terminais, terminais in self.gramatica.conjunto_producoes.iteritems():
            linha = '%s -> %s' % (nao_terminais, '|'.join(terminais))
            linhas.append(linha)

        return '{\n%s\n}' % self.__lista_para_string(linhas, 2)

    def gerar(self):
        str = 'G = (%s, %s, P, S)' % (self.simbolos_nao_terminais, self.simbolos_terminais)
        str += '\nP = %s' % self.conjunto_producoes
        return str

    def __lista_para_string(self, lista, nivel_identacao):
        identacao = nivel_identacao * ' '
        return '\n'.join([identacao + item for item in lista])

    def __gerar_simbolos(self, simbolos):
        return '{' + ', '.join(simbolos) + '}'