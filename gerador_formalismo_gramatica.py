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
        str = '{'

        for nao_terminais, terminais in self.gramatica.conjunto_producoes.iteritems():
            str += "\n  " + nao_terminais + ' -> '
            str += '|'.join(terminais)

        str += "\n}"
        return str

    def gerar(self):
        str = 'G = (%s, %s, P, S)' % (self.simbolos_nao_terminais, self.simbolos_terminais)
        str += "\nP = %s" % self.conjunto_producoes
        return str

    def __gerar_simbolos(self, simbolos):
        return '{' + ', '.join(simbolos) + '}'