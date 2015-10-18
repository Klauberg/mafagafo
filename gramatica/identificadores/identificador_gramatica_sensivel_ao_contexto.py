# -*- coding: utf-8 -*-
import re
from gramatica.util import *
from constants import *

class IdentificadorGramaticaSensivelAoContexto:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(self.esquerda_menor_que_direita(e, d) for e, d in self.gramatica.conjunto_producoes.iteritems())

    def lado_direito_valido(self):
        return all(self.sentencas_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def sentencas_validas(self, sentencas):
        return all(not sentenca_eh_vazia(x) for x in sentencas)

    def esquerda_menor_que_direita(self, esquerda, direita):
        return all(len(esquerda) <= len(sentenca) for sentenca in direita)