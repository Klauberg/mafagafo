# -*- coding: utf-8 -*-
import re
from constants import *

class IdentificadorGramaticaIrrestrita:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return all(self.contem_nt(x) for x in self.gramatica.conjunto_producoes)

    def contem_nt(self, x):
        """Verifica se a string contém símbolo não-terminal"""
        return bool(re.search('[A-Z]', x))