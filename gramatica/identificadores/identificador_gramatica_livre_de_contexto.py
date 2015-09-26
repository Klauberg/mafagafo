# -*- coding: utf-8 -*-
import re

class IdentificadorGramaticaLivreDeContexto:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(self.apenas_um_nt(x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.partes_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def partes_validas(self, partes):
        return all(self.nao_contem_sentenca_vazia(x) for x in partes)

    def apenas_um_nt(self, x):
        """Verifica se em uma string há apenas um símbolo não-terminal"""
        return re.match('^[A-Z]$', x)

    def nao_contem_sentenca_vazia(self, str):
        return not 'X' in str # X = sentença vazia