# -*- coding: utf-8 -*-
import re
from constants import *

class IdentificadorGramaticaLivreDeContexto:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(self.apenas_um_nt(x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.sentencas_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def sentencas_validas(self, sentencas):
        return all(self.nao_eh_sentenca_vazia(x) for x in sentencas)

    def apenas_um_nt(self, x):
        """Verifica se a string é apenas um símbolo não-terminal"""
        return re.match('^[A-Z]$', x)

    def nao_eh_sentenca_vazia(self, str):
        return str != ''