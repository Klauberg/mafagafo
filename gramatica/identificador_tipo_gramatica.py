from identificadores import *

class IdentificadorTipoGramatica:
    def __init__(self, gramatica):
        self.gramatica = gramatica

    def identificar(self):
        if IdentificadorGramaticaRegular(self.gramatica).identificar():
            return 'GR'

        if IdentificadorGramaticaLivreDeContexto(self.gramatica).identificar():
            return 'GLC'

        if IdentificadorGramaticaSensivelAoContexto(self.gramatica).identificar():
            return 'GSC'

        if IdentificadorGramaticaIrrestrita(self.gramatica).identificar():
            return 'GI'

        return None