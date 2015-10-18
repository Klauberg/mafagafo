# -*- coding: utf-8 -*-
import re
from gramatica.util import *
from constants import *

class IdentificadorGramaticaLivreDeContexto:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(sentenca_eh_1nt(x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.sentencas_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def sentencas_validas(self, sentencas):
        return all(not sentenca_eh_vazia(x) for x in sentencas)