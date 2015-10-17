# -*- coding: utf-8 -*-
from gramatica import *
from interface import interface_gramatica
from gramatica.arvore_derivacoes.arvore_derivacoes import *

#g = Gramatica(['S', 'A', 'B'], ['a', 'b', 'c', 'd'], {
#    'S': ['aBAa'],
#    'A': ['b', 'cA'],
#    'B': ['c', 'd'] #, 'BA': 'c'
#})
#ad = ArvoreDerivacoes(g)
#ad.montar_sem_recursao()
#print [x.sentenca for x in ad.folhas]
#print ad.buscar_sentencas_minimas()

interface_gramatica.iniciar()