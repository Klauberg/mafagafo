# -*- coding: utf-8 -*-
import re
from constants import *

class NoArvoreDerivacoes:
    def __init__(self, sentenca, nodo_pai = None):
        self.sentenca = sentenca
        self.nodo_pai = nodo_pai
        self.nos = []

    def nao_terminais_derivados(self):
        """Busca símbolos não-terminais encontrados nos nós pais"""
        nao_terminais = set()
        no = self.nodo_pai
        while no is not None:
            nao_terminais.update(self.buscar_nts(no.sentenca))
            no = no.nodo_pai
        return nao_terminais

    # to-do: mover esse método para classe utilitária
    def buscar_nts(self, sentenca):
        """Busca símbolos NT em uma sentença"""
        return set(re.findall('[A-Z]', sentenca))

    # to-do: mover esse método para classe utilitária
    def eh_sentenca_final(self):
        """Verifica se a sentença é final, isto é, se não possui NTs"""
        return not self.buscar_nts(self.sentenca)