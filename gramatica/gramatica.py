class Gramatica:
    def __init__(self, simbolos_nao_terminais, simbolos_terminais, conjunto_producoes, simbolo_inicial):
        self.simbolos_nao_terminais = simbolos_nao_terminais
        self.simbolos_terminais = simbolos_terminais
        self.conjunto_producoes = conjunto_producoes
        self.simbolo_inicial = simbolo_inicial

