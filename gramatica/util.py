# -*- coding: utf-8 -*-
import re

def sentenca_contem_nt(str):
    """Verifica se a string contém símbolo não-terminal"""
    return bool(re.search('[A-Z]', str))

def sentenca_eh_final(str):
    """Verifica se uma sentença é final, isto é, não possui símbolos não-terminais"""
    return not sentenca_contem_nt(str)

def sentenca_eh_1nt(str):
    """Verifica se a string é apenas um símbolo não-terminal"""
    return bool(re.match('^[A-Z]$', str))

def sentenca_eh_vazia(str):
    """Verifica se a sentença é vazia"""
    return str == ''

def buscar_nts(str):
    """Busca símbolos NT em uma sentença"""
    return set(re.findall('[A-Z]', str))