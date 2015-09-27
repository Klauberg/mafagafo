# -*- coding: utf-8 -*-
import re
from constants import *

def validar_simbolos_nt(simbolos):
    """Valida os símbolos não-terminais entrados pelo usuário"""
    if not simbolos or simbolos[0].strip() == '':
        return (False, 'Nenhum símbolo preenchido')

    if not all(re.match('^[A-Z]$', s) for s in simbolos):
        return (False, 'Cada símbolo não-terminal deve ser uma letra maiúscula (A-Z).')

    if not SIMBOLO_INICIAL in simbolos:
        return (False, 'Símbolo inicial (%s) deve estar incluso na lista.' % SIMBOLO_INICIAL)

    validacao_sv = validar_sentenca_vazia(simbolos)
    if not validacao_sv[0]:
        return validacao_sv

    return (True,)

def validar_simbolos_t(simbolos):
    """Valida os símbolos terminais entrados pelo usuário"""
    if not simbolos or simbolos[0].strip() == '':
        return (False, 'Nenhum símbolo preenchido')

    if not all(re.match('^[a-z0-9]$', s) for s in simbolos):
        return (False, 'Cada símbolo terminal deve ser uma letra minúscula (a-z) ou dígito (0-9).')

    validacao_sv = validar_sentenca_vazia(simbolos)
    if not validacao_sv[0]:
        return validacao_sv

    return (True,)

def validar_sentenca_vazia(simbolos):
    if any(s == SIMBOLO_SENTENCA_VAZIA for s in simbolos):
        return (False, 'Você não pode informar o símbolo %s aqui, pois ele é o caractere' \
            'que representa a sentença vazia nesse programa.' % SIMBOLO_SENTENCA_VAZIA)

    return (True,)