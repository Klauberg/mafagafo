# -*- coding: utf-8 -*-
import re
from constants import *
from arvore_derivacoes import ArvoreDerivacoes

class IdentificadorLinguagemGramatica:
    def __init__(self, gramatica):
        self.gramatica = gramatica
        self.arvore_derivacoes = ArvoreDerivacoes(gramatica).montar_sem_recursao()

    def identificar(self):
        sentencas = [no.sentenca for no in self.arvore_derivacoes.folhas]

        if any(self.contem_nt(s) for s in sentencas):
            return self.inferir_linguagem()
        else:
            sentencas = [SIMBOLO_SENTENCA_VAZIA if s == '' else s for s in sentencas]
            return '{%s}' % (', '.join(sentencas))

    def inferir_linguagem(self):
        return 'TO-DO'

    # to-do: mover este método para outra classe utilitária, pois está repetido
    # em outras classes
    def contem_nt(self, x):
        """Verifica se a string contém símbolo não-terminal"""
        return bool(re.search('[A-Z]', x))