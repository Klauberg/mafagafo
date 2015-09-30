import re
from constants import *

class IdentificadorLinguagem:

    limite = 5 #determina o limite da busca em largura

    def __init__(self, gramatica):
        self.gramatica = gramatica

    def buscarSentencasMinimas(self, estado, sentencasMinimas):        
        
        #busca por largura
        
        return sentenca

    #retorna a quantidade de simbolos nao terminais de um conjunto
    def getQuantidadeNaoTerminais(self, conjunto):
        count = 0
        for x in conjunto #para cada símbolo do conjunto
            if(bool(re.search('[a-z]', x) | bool(re.search('[0-9]', x))) # verifica se é um não terminal
                count+=1
        return count
