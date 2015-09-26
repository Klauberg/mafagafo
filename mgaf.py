from gramatica import Gramatica
from gerador_formalismo_gramatica import GeradorFormalismoGramatica

gramatica = Gramatica(['S'], ['a', 'b'], {'S': ['a', 'b'], 'SS': ['b']})
gerador_formalismo_gramatica = GeradorFormalismoGramatica(gramatica)

print gerador_formalismo_gramatica.gerar()