import re

class IdentificadorGramaticaRegular:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        return self.lado_esquerdo_valido() and self.lado_direito_valido()

    def lado_esquerdo_valido(self):
        return all(re.match('^[A-Z]$', x) for x in self.gramatica.conjunto_producoes)

    def lado_direito_valido(self):
        return all(self.partes_validas(x) for x in self.gramatica.conjunto_producoes.values())

    def partes_validas(self, partes):
        return all(re.match('^[a-z0-9][A-Z]?$', x) for x in partes)