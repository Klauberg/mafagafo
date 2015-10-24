# -*- coding: utf-8 -*-
import re
from constants import *

def validar_sentenca_vazia(simbolo):
    if any(s == SIMBOLO_SENTENCA_VAZIA for s in simbolos):
        return (False, 'Você não pode informar o símbolo %s aqui, pois ele é o caractere' \
            'que representa a sentença vazia nesse programa.' % SIMBOLO_SENTENCA_VAZIA)

    return (True,)

def validar_lado_esquerdo(simbolos):
    if not re.search('[A-Z]', simbolos):
        return (False, 'O lado esquerdo deve conter ao menos um símbolo não-terminal')

    return (True,)

def validar_producao(producao):
    if not ':' in producao:
        return (False, 'Produção inválida')

    return (True,)