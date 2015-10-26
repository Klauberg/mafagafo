# -*- coding: utf-8 -*-
import sys
import validacoes
from gramatica import *
from constants import *
from gramatica.arvore_derivacoes import ArvoreDerivacoes

def ler_conjunto_producoes(simbolos_nt, simbolos_t):
    print 'Manipulador de Gramáticas e Autômatos Finitos'
    print '---------------------------------------------'
    print 'Insira as produções da gramática para cada símbolo, uma por linha.'
    print 'Use o caractere : para separar o lado da esquerda do lado da direita.'
    print 'Use | para separar as produções.'
    print 'O símbolo não-terminal à esquerda no primeiro conjunto de produções será o inicial.'
    print 'Exemplo: S:aA|a'
    print '         A:b|aA'
    print
    print 'Digite abaixo:'

    simbolo_inicial = None
    conjunto_producoes = {}
    while True:
        raw = raw_input()
        
        if raw.strip() == '':
            break

        verificar_validacao(validacoes.validar_producao(raw))

        esquerda = raw.split(':')[0].strip()
        direita = raw.split(':')[1].strip()

        if simbolo_inicial is None:
            simbolo_inicial = esquerda

        for c in esquerda:
            if not c == SIMBOLO_SENTENCA_VAZIA:
                if c.isupper():
                    adicionar_novo_simbolo(simbolos_nt, c)
                else:
                    adicionar_novo_simbolo(simbolos_t, c)

        for c in direita.replace('|', ''):
            if not c == SIMBOLO_SENTENCA_VAZIA:
                if c.isupper():
                    adicionar_novo_simbolo(simbolos_nt, c)
                else:
                    adicionar_novo_simbolo(simbolos_t, c)    

        esquerda = raw[:raw.index(':')]
        validacao = validacoes.validar_lado_esquerdo(esquerda)
        verificar_validacao(validacao)
        
        ler_linha_conjunto_producoes(raw, conjunto_producoes)

    validacao = validacoes.validar_conjunto_producoes(conjunto_producoes, simbolos_nt)
    verificar_validacao(validacao)

    return (simbolo_inicial, conjunto_producoes)

def adicionar_novo_simbolo(lista, simbolo):
    for s in lista:
        if s == simbolo:
            return None
    lista.append(simbolo)
    return None

def ler_linha_conjunto_producoes(linha, conjunto_producoes):
    separacao = linha.split(':')
    if len(separacao) != 2:
        print 'Erro de formato'
        sys.exit()

    esquerda = separacao[0].strip()
    direita = separacao[1]
    partes = direita.replace(SIMBOLO_SENTENCA_VAZIA, '').split('|')
    conjunto_producoes[esquerda] = partes

def verificar_validacao(validacao):
    """
    Verifica se uma tupla validação está ok.
    Se não estiver, imprime a mensagem e encerra o programa
    """
    if not validacao[0]:
        print validacao[1]
        sys.exit()

def imprimir_derivacoes_sentencas(nos):
    if nos is None:
        print ('Não é possível gerar sentenças para esta gramática, pois ela não gera'
               ' nenhuma sentença finita.')
        return

    for no in nos:
        derivacoes = []
        pai = no.nodo_pai
        while pai is not None:
            derivacoes.insert(0, pai.sentenca)
            pai = pai.nodo_pai

        print (' -> '.join(derivacoes)) + ' -> ' + (SIMBOLO_SENTENCA_VAZIA if no.sentenca == '' else no.sentenca)

def imprimir_linguagem(linguagem):
    if linguagem is None:
        print 'Não é possível identificar a linguagem dessa gramática, pois ela não ' \
              'é capaz de gerar nenhuma sentença finita.'
    else:
        print linguagem

def iniciar():
    simbolos_nt = []
    simbolos_t = []
    simbolo_inicial, conjunto_producoes = ler_conjunto_producoes(simbolos_nt, simbolos_t)
    gramatica = Gramatica(simbolos_nt, simbolos_t, conjunto_producoes, simbolo_inicial)

    formalizacao = GeradorFormalismoGramatica(gramatica).gerar()
    print 'Formalização:\n%s\n' % formalizacao

    tipo = IdentificadorTipoGramatica(gramatica).identificar()
    print 'Tipo de gramática:\n%s\n' % tipo

    linguagem = IdentificadorLinguagemGramatica(gramatica).identificar()
    print 'Linguagem:'
    imprimir_linguagem(linguagem)
    print

    gerador_sentencas = GeradorSentencas(gramatica)
    sentencas_geradas = gerador_sentencas.gerar(10)
    print 'Sentenças geradas:'
    imprimir_derivacoes_sentencas(sentencas_geradas)