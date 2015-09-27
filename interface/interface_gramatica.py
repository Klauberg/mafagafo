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
    pass

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
    simbolos_t = ler_simbolos_t()
    conjunto_producoes = ler_conjunto_producoes(simbolos_nt, simbolos_t)

    print 'NT: ' + ','.join(simbolos_nt)
    print 'T: ' + ','.join(simbolos_t)