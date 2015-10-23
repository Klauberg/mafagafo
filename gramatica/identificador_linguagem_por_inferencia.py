# -*- coding: utf-8 -*-
import re
import sys
from constants import *

class IdentificadorLinguagemPorInferencia:
    ALFABETO_VARIAVEIS = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']

    def __init__(self, sentencas):
        self.sentencas = sentencas

    def identificar(self):
        lista = {} # lista que representa cada sentenca
        for s in self.sentencas:
            for c in s:
                lista.update({c:'-'})
        for l in lista:
            vmin = self.verificar_minimo(l)
            lista.update({l:'>='+str(vmin)})
        for l in lista:
            for l2 in lista:
                if l!=l2 and self.verificar_multiplo(l, l2)!=0:
                    lista[l] = '='+str(self.verificar_multiplo(l, l2))+l2 

        return self.formalizar(lista)

    def formalizar(self, lista):
        variaveis = {}
        count = 0
        for l in lista:
            if not lista[l] in variaveis:
                variaveis.update({lista[l]:self.ALFABETO_VARIAVEIS[count]})
                count+=1

        lista_simbolos = []
        for l in lista:
            lista_simbolos.append(l+'^'+variaveis[lista[l]])

        quantidades_simbolos = []
        for v in variaveis:
            if not '>' in v:
                last = v[-1] # pega o ultimo caractere v = '=2a' -> last = 'a'
                quantidades_simbolos.append(variaveis[v]+v.replace(last, variaveis[lista[last]]))
            else:
                quantidades_simbolos.append(variaveis[v]+str(v))

        return 'L = { %s | %s }' % (', '.join(lista_simbolos), ', '.join(quantidades_simbolos))

    def verificar_multiplo(self, t1, t2):
        div = 0
        for s in self.sentencas:
            if t1 in s and t2 in s:
                if s.count(t2) == 0: return 0
                if div == 0:
                    div = s.count(t1)/s.count(t2)
                elif div != s.count(t1)/s.count(t2):
                    return 0
        if div == 1: return 0
        return div

    def verificar_minimo(self, t):
        minimo = sys.maxsize
        for s in self.sentencas:
            if s.count(t) < minimo:
                minimo = s.count(t)
        return minimo