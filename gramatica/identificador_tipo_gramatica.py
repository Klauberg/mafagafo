# -*- coding: utf-8 -*-
from identificadores import *

class IdentificadorTipoGramatica:
    # esquerda = sigla que representa o tipo de gramática
    # direita = classe do identificador de tipo de gramática correspondente
    IDENTIFICADORES = {
        'GR': IdentificadorGramaticaRegular,
        'GLC': IdentificadorGramaticaLivreDeContexto,
        'GSC': IdentificadorGramaticaSensivelAoContexto,
        'GI': IdentificadorGramaticaIrrestrita
    }

    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        for sigla, classe in self.IDENTIFICADORES.iteritems():
            if classe(self.gramatica).identificar():
                return sigla

        return None