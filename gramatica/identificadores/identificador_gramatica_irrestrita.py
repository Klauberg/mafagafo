# -*- coding: utf-8 -*-
import re
from gramatica.util import *
from constants import *

class IdentificadorGramaticaIrrestrita:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return all(sentenca_contem_nt(x) for x in self.gramatica.conjunto_producoes)