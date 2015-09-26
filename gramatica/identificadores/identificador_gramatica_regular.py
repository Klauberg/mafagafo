# -*- coding: utf-8 -*-
import re

class IdentificadorGramaticaRegular:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(self.apenas_um_nt(x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.partes_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def partes_validas(self, partes):
        return all(self.t_ou_t_seguido_de_nt(x) for x in partes)

    def apenas_um_nt(self, x):
        """Verifica se a string é apenas um símbolo não-terminal"""
        return re.match('^[A-Z]$', x)

    def t_ou_t_seguido_de_nt(self, x):
        """Verifica se a string é composta por um símbolo terminal ou
        um terminal seguido de não-terminal"""
        return re.match('^[a-z0-9][A-Z]?$', x)