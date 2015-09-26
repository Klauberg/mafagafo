from gramatica.gramatica import Gramatica
from gramatica.gerador_formalismo_gramatica import GeradorFormalismoGramatica
from gramatica.identificador_tipo_gramatica import IdentificadorTipoGramatica

gramatica = Gramatica(['S'], ['a', 'b'], {'S': ['a', 'b'], 'SS': ['b']})

# gera formalismo
gerador_formalismo_gramatica = GeradorFormalismoGramatica(gramatica)
print gerador_formalismo_gramatica.gerar()

# identifica tipo
identificador_tipo_gramatica = IdentificadorTipoGramatica(gramatica)
print identificador_tipo_gramatica.identificar()