# -*- coding: utf-8 -*-
import re
from constants import *

def validar_lado_esquerdo(simbolos):
    if not re.search('[A-Z]', simbolos):
        return (False, 'O lado esquerdo deve conter ao menos um símbolo não-terminal')

    if SIMBOLO_SENTENCA_VAZIA in simbolos:
        return (False, 'O símbolo de sentença vazia (%s) não pode estar no lado esquerdo' \
            ' do conjunto de produções.' % SIMBOLO_SENTENCA_VAZIA)

    return (True,)

def validar_producao(producao):
    if not ':' in producao:
        return (False, 'Produção inválida')

    return (True,)

def validar_conjunto_producoes(conjunto_producoes, simbolos_nt):
    if not all(any(nt in p for p in conjunto_producoes)for nt in simbolos_nt):
        return (False, 'Símbolo não terminal está sem produção')
    
    return (True,)