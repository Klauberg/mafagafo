# -*- coding: utf-8 -*-
import re
from no_arvore_derivacoes import *
from gerador_derivacoes import *
from constants import *
from collections import deque

class ArvoreDerivacoes:
    def __init__(self, gramatica):
        self.gramatica = gramatica
        self.gerador_derivacoes = GeradorDerivacoes(gramatica)
        self.limpar_arvore()

    def limpar_arvore(self):
        self.raiz = NoArvoreDerivacoes(SIMBOLO_INICIAL)
        self.folhas = [self.raiz]

    def montar_sem_recursao(self):
        self.limpar_arvore()
        while self.gerar_novo_nivel(True):
            pass

    def gerar_novo_nivel(self, impedir_recursao):
        progresso = False
        nova_lista_folhas = []

        for no in self.folhas:
            if not self.contem_nt(no.sentenca):
                nova_lista_folhas.append(no)
                continue

            if impedir_recursao and no.contem_recursao():
                nova_lista_folhas.append(no)
                continue

            progresso = True
            derivacoes = self.gerador_derivacoes.gerar_derivacoes(no.sentenca)
            for derivacao in derivacoes:
                nova_folha = NoArvoreDerivacoes(derivacao, no)
                no.nos.append(nova_folha)
                nova_lista_folhas.append(nova_folha)

        if progresso:
            self.folhas = nova_lista_folhas

        return progresso

    def pode_gerar_sentenca_finita(self):
        """Verifica se a gramática pode gerar ao menos uma sentença finita"""
        return any(not self.contem_nt(no.sentenca) for no in self.folhas)

    def buscar_sentencas_minimas(self):
        """Busca sentenças mínimas da gramática"""
        sentencas_minimas = []
        sentencas_finais = [no.sentenca for no in self.folhas if no.eh_sentenca_final()]

        if sentencas_finais:
            tamanho_minimo = len(min(sentencas_finais, key = lambda s: len(s)))
            sentencas_minimas = [s for s in sentencas_finais if len(s) == tamanho_minimo]
        
        return sentencas_minimas

    #def __buscar_folhas(self):
    #    """Busca folhas (nós terminais) da árvore"""
    #    folhas = []
    #    fila_nos = deque([self.raiz])
    #
    #    while fila_nos:
    #        no = fila_nos.popleft()
    #        fila_nos.extend(no.nos)
    #        if not no.nos:
    #            folhas.append(no)
    #
    #    return folhas

    # to-do: mover este método para outra classe utilitária, pois está repetido
    # em outras classes
    def contem_nt(self, x):
        """Verifica se a string contém símbolo não-terminal"""
        return bool(re.search('[A-Z]', x))