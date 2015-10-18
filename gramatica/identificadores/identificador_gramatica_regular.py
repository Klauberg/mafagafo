# -*- coding: utf-8 -*-
import re
from gramatica.util import *
from constants import *

class IdentificadorGramaticaRegular:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(sentenca_eh_1nt(x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.partes_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def partes_validas(self, partes):
        return all(self.t_ou_t_seguido_de_nt(x) for x in partes)

    def t_ou_t_seguido_de_nt(self, x):
        """Verifica se a string é composta por um símbolo terminal ou
        um terminal seguido de não-terminal"""
        return bool(re.match('^[a-z0-9][A-Z]?$', x))