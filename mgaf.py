from gramatica.gramatica import Gramatica
from gramatica.gerador_formalismo_gramatica import GeradorFormalismoGramatica

gramatica = Gramatica(['S'], ['a', 'b'], {'S': ['a', 'b'], 'SS': ['b']})

# gera formalismo
gerador_formalismo_gramatica = GeradorFormalismoGramatica(gramatica)
print gerador_formalismo_gramatica.gerar()