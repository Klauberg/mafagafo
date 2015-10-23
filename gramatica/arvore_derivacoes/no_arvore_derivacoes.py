# -*- coding: utf-8 -*-
import re
from gramatica.util import *
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
            nao_terminais.update(buscar_nts(no.sentenca))
            no = no.nodo_pai
        return nao_terminais

    def contem_recursao(self):
        """
        Verifica se o nó contém recursão.
        Isso acontece se o conjunto de NT na sentença desse nó faz parte
        do conjunto de NTs pelo qual a sentença do nó atual já passou para
        ter sido derivada
        """
        nts = buscar_nts(self.sentenca)
        return self.nao_terminais_derivados().issuperset(nts)

    def quantidade_derivacoes(self):
        """
        Conta quantidade de derivações feitas até este nó
        """
        pai = self.nodo_pai
        i = 0
        while pai is not None:
            i += 1
            pai = pai.nodo_pai
        return i