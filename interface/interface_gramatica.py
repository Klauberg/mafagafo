# -*- coding: utf-8 -*-
import sys
import validacoes
from gramatica import *
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
    print 'Exemplo: %s:aA|a' % SIMBOLO_INICIAL
    print '         A:b|aA'
    print
    print 'Digite abaixo:'

    conjunto_producoes = {}
    while True:
        raw = raw_input()
        if raw.strip() == '':
            break
        ler_linha_conjunto_producoes(raw, conjunto_producoes)

    return conjunto_producoes

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

def iniciar():
    simbolos_nt = ler_simbolos_nt()
    print

    simbolos_t = ler_simbolos_t()
    print

    conjunto_producoes = ler_conjunto_producoes(simbolos_nt, simbolos_t)
    gramatica = Gramatica(simbolos_nt, simbolos_t, conjunto_producoes)
    tipo = IdentificadorTipoGramatica(gramatica).identificar()
    formalizacao = GeradorFormalismoGramatica(gramatica).gerar()
    gerador_sentencas = GeradorSentencas(gramatica)

    print 'Formalização:\n%s\n' % formalizacao
    print 'Tipo de gramática: %s\n' % tipo

    print 'Sentenças geradas:'
    for x in range(0, 3):
        gerado = gerador_sentencas.gerar()
        print ' -> '.join(gerado[1])