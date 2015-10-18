# -*- coding: utf-8 -*-
import re
from gerador_sentencas import *
from identificador_linguagem_por_inferencia import *
from constants import *
from arvore_derivacoes import ArvoreDerivacoes
from util import *

class IdentificadorLinguagemGramatica:
    def __init__(self, gramatica):
        self.gramatica = gramatica
        self.arvore_derivacoes = ArvoreDerivacoes(gramatica).montar_sem_recursao()

    def identificar(self):
        sentencas = [no.sentenca for no in self.arvore_derivacoes.folhas]

        if any(sentenca_contem_nt(s) for s in sentencas):
            return self.inferir_linguagem()
        else:
            sentencas = [SIMBOLO_SENTENCA_VAZIA if s == '' else s for s in sentencas]
            return '{%s}' % (', '.join(sentencas))

    def inferir_linguagem(self):
        gerador_sentencas = GeradorSentencas(self.gramatica)
        sentencas_geradas = [no.sentenca for no in gerador_sentencas.gerar(100)]
        return IdentificadorLinguagemPorInferencia(sentencas_geradas).identificar()