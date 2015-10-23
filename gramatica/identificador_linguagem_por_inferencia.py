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
            lista.update({l:vmin})
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
        print variaveis
        for l in lista:
            print 
            valor += l+'^'+variaveis[lista[l]]+', '
        valor += '|'
        for v in variaveis:
            valor += variaveis[v]+'>='+str(v)+', '
        valor += ')'
        return valor

    def verificarMultiplo(self, t1, t2):
        div = 0
        for s in self.sentencas:
            if t1 in s and t2 in s:
                if div == 0:
                    div = self.sentencas.count(t1)/self.sentencas.count(t2)
                else:
                    if div != self.sentencas.count(t1)/self.sentencas.count(t2):
                        return 0
        return div

    def verificarMinimo(self, t):
        minimo = 999999 # sys.maxsize não ta funcionando
        for s in self.sentencas:
            if s.count(t) < minimo:
                minimo = s.count(t)
        return minimo