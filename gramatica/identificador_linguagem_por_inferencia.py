# -*- coding: utf-8 -*-
import re
from constants import *

class IdentificadorLinguagemPorInferencia:
    def __init__(self, sentencas):
        self.sentencas = sentencas

    def identificar(self):
        # Implementar lógica aqui
        # Dá para acessar as sentenças geradas aqui por self.sentencas
        #print '\n'.join(self.sentencas)

        lista = {} #lista que representa cada sentenca
        for s in self.sentencas:
            for c in s:
                lista.update({c:'-'})
        for l in lista:
            vmin = self.verificarMinimo(l)
            lista.update({l:'>='+str(vmin)})
        for l in lista:
            for l2 in lista:
                if l!=l2 and self.verificarMultiplo(l, l2)!=0:
                    lista[l] = '='+str(self.verificarMultiplo(l, l2))+l2 

        return self.formalizar(lista)

    def formalizar(self, lista):
        alfabetoVariaveis = ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
        valor = 'L=('
        variaveis = {}
        count = 0
        for l in lista:
            if not lista[l] in variaveis:
                variaveis.update({lista[l]:alfabetoVariaveis[count]})
                count+=1
        for l in lista:
            valor += l+'^'+variaveis[lista[l]]+', '
        valor += '|'
        for v in variaveis:
            if not '>' in v:
                last = v[-1] #pega o ultimo caractere v = '=2a' -> last = 'a'
                valor += variaveis[v]+v.replace(last, variaveis[lista[last]])+', '
            else:
                valor += variaveis[v]+str(v)+', '
        valor += ')'
        return valor

    def verificarMultiplo(self, t1, t2):
        div = 0
        for s in self.sentencas:
            if t1 in s and t2 in s:
                if s.count(t2) == 0: return 0
                if div == 0:
                    div = s.count(t1)/s.count(t2)
                else:
                    if div != s.count(t1)/s.count(t2):
                        return 0
        if div == 1: return 0
        return div

    def verificarMinimo(self, t):
        minimo = 999999 # sys.maxsize não ta funcionando
        for s in self.sentencas:
            if s.count(t) < minimo:
                minimo = s.count(t)
        return minimo