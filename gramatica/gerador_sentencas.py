# -*- coding: utf-8 -*-
import re
from constants import *
from arvore_derivacoes import ArvoreDerivacoes

class GeradorSentencas:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def gerar(self, quantidade_requisitada):
        arvore_derivacoes = ArvoreDerivacoes(self.gramatica).montar_sem_recursao()
        if not arvore_derivacoes.pode_gerar_sentenca_finita():
            return None
        
        quantidade_gerada_anterior = 0
        while True:
            nos_finais = arvore_derivacoes.buscar_nos_de_sentencas_finais()
            quantidade_gerada = len(nos_finais)

            if len(arvore_derivacoes.folhas) == len(nos_finais) or quantidade_gerada >= quantidade_requisitada:
                nos_finais.sort(key = lambda x: x.quantidade_derivacoes())
                if quantidade_gerada > quantidade_requisitada:
                    nos_finais = nos_finais[:quantidade_requisitada]
                return nos_finais

            arvore_derivacoes.gerar_novo_nivel(False)