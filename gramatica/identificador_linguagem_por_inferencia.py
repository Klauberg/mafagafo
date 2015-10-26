# -*- coding: utf-8 -*-
import re
import sys
from constants import *

class IdentificadorLinguagemPorInferencia:
    #usar apenas um caractere por variavel
    ALFABETO_VARIAVEIS = ['m', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']

    def __init__(self, sentencas):
        self.sentencas = sentencas

    def identificar(self):
        lista = {} #lista que representa cada sentença
        count = 0
        for s in self.sentencas:
            for c in s:
                lista.update({c:'-'})
        for l in lista:
            for l2 in lista:
                if self.verificar_mesma_quantidade(l):
                    vmin = self.verificar_minimo(l)
                    lista[l] = self.ALFABETO_VARIAVEIS[count]+'='+str(vmin)
                    count+=1
                elif l!=l2 and self.verificar_mesma_quantia(l, l2):
                    vmin = self.verificar_minimo(l)
                    lista[l] = self.ALFABETO_VARIAVEIS[count]+'>='+str(vmin)
                    lista[l2] = self.ALFABETO_VARIAVEIS[count]+'>='+str(vmin)
                    count+=1
                elif l!=l2 and self.verificar_multiplo(l, l2)!=0:
                    if lista[l2][0] == '-':
                        vmin = self.verificar_minimo(l2)
                        lista[l2] = self.ALFABETO_VARIAVEIS[count]+'>='+str(vmin)
                        count+=1 
                    lista[l] = self.ALFABETO_VARIAVEIS[count]+'='+str(self.verificar_multiplo(l, l2))+lista[l2][0]
                    count+=1
                elif lista[l]=='-':
                    vmin = self.verificar_minimo(l)
                    lista[l] = self.ALFABETO_VARIAVEIS[count]+'>='+str(vmin)
                    count+=1                
        return self.formalizar(lista)

    def formalizar(self, lista):
        lista_simbolos = []
        for l in lista:
            lista_simbolos.append(l+'^'+lista[l][0])

        quantidades_simbolos = []
        for l in lista:
            if not any(lista[l][0] in q[0] for q in quantidades_simbolos):
                quantidades_simbolos.append(lista[l])

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

    def verificar_mesma_quantia(self, t1, t2):
        for s in self.sentencas:
            if s.count(t1) != s.count(t2):
                return False
        return True

    def verificar_mesma_quantidade(self, t1):
        quantidade = -1
        for s in self.sentencas:
            if quantidade == -1:
                quantidade = s.count(t1)
            elif s.count(t1) != quantidade:
                return False
        return True