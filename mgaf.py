from gramatica import *

gramatica = Gramatica(['S'], ['a', 'b'], {'S': ['a', 'b'], 'SS': ['b']})

# gera formalismo
gerador_formalismo_gramatica = GeradorFormalismoGramatica(gramatica)
print gerador_formalismo_gramatica.gerar()

# identifica tipo
identificador_tipo_gramatica = IdentificadorTipoGramatica(gramatica)
print identificador_tipo_gramatica.identificar()