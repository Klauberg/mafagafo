# -*- coding: utf-8 -*-
import sys
import validacoes
from gramatica import *
from gramatica.arvore_derivacoes import ArvoreDerivacoes
from constants import *

def ler_simbolos_nt():
    """Le e valida os simbolos não-terminais"""
    print 'Preencha os símbolos não terminais separados por vírgula:'
    raw = raw_input()
    simbolos = remover_duplicados(raw.split(','))
    validacao = validacoes.validar_simbolos_nt(simbolos)
    verificar_validacao(validacao)
    simbolos.insert(0, simbolos.pop(simbolos.index(SIMBOLO_INICIAL)))
    return simbolos

def ler_simbolos_t():
    """Le e valida os simbolos terminais"""
    print 'Preencha os símbolos terminais separados por vírgula:'
    raw = raw_input()
    simbolos = remover_duplicados(raw.split(','))
    validacao = validacoes.validar_simbolos_t(simbolos)
    verificar_validacao(validacao)
    return simbolos

def ler_conjunto_producoes(simbolos_nt, simbolos_t):
    print 'Insira as produções para cada símbolo, uma por linha.'
    print 'Use o caractere : para separar o lado da esquerda do lado da direita.'
    print 'Use | para separar as partes da produção.'
    print 'O símbolo à esquerda no primeiro conjunto de produções será o inicial.'
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

    return (simbolo_inicial, conjunto_producoes)

def adicionar_novo_simbolo(lista, simbolo):
    for s in lista:
        if s == simbolo:
            return None
    lista.append(simbolo)
    return None

def buscar_simbolos_t(conjunto_producoes):
    for s in conjunto_producoes:
        print s[0]
        print s[1]
        print 
    return None

def buscar_simbolos_nt(conjunto_producoes):
    return None

def ler_linha_conjunto_producoes(linha, conjunto_producoes):
    separacao = linha.split(':')
    if len(separacao) < 2:
        print 'Erro de formato'
        return

    esquerda = separacao[0].strip()
    direita = separacao[1]
    partes = direita.replace(SIMBOLO_SENTENCA_VAZIA, '').split('|')
    conjunto_producoes[esquerda] = partes

def remover_duplicados(lista):
    return sorted(set(lista))

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
    print 'Linguagem:\n%s\n' % linguagem

    gerador_sentencas = GeradorSentencas(gramatica)
    sentencas_geradas = gerador_sentencas.gerar(10)
    print 'Sentenças geradas:'
    imprimir_derivacoes_sentencas(sentencas_geradas)