# Mafagafo

Manipulador de Gramáticas ~~e Autômatos Finitos~~

Trabalho Prático de Linguagens Formais - UNISC 2015/2

Alunos: Eduardo Cortes, Guilherme Sehn, Gustavo Marchesan

![mafagafo](https://cloud.githubusercontent.com/assets/830208/10118867/a42e6040-645a-11e5-8fbe-29333ffdf074.png)

## Como funciona
Uma gramática formal é formalmente definida como uma tupla (*N*, *Σ*, *P*, *S*), onde:

- *N* é o conjunto finito de símbolos não-terminais usados na gramática, que neste programa são representados por caracteres maiúsculos (A-Z), com exceção de X, que representa sentença vazia.
- *Σ* é o conjunto finito de símbolos terminais usados na gramática, que neste programa são representados por caracteres minúsculos (a-z).
- *P* é um conjunto finito de regras de produção.
- *S* é o símbolo não-terminal inicial, que deve estar na lista de não-terminais (*S* ∈ *N*)

Com isso, podemos definir um exemplo de gramática:

```
G = ({S, A}, {a, b}, P, S)
P = {
  S → aA|a
  A → b|aA
}
```

Para utilizar este programa, po usuário precisa entrar com a definição da gramática. Para isso, o usuário deve iniciar com as regras de produção, separando o lado da esquerda do lado direito com o caractere `:`. Para a gramática do exemplo acima, o usuário deve digitar a seguinte entrada, utilizando a tecla <kbd>Enter</kbd> para quebrar as linhas:

```
S:aA|a
A:b|aA
```

Para finalizar a entrada das regras de inclusão, teclar <kbd>Enter</kbd> mais uma vez.

A partir das regras de produção, o programa irá automaticamente extrair os símbolos terminais (*N*), não-terminais (*Σ*) e símbolo inicial (*S*). O símbolo ao lado esquerdo do primeiro conjunto de regras é definido como símbolo inicial (*S*).

A partir dos dados extraídos, o aplicativo irá:

- Gerar o formalismo da gramática
- Identificar o tipo (GI - gramática irregular, GSC - gramática sensível ao contexto, GLC - gramática livre de contexto, GR - gramática regular)
- Gerar um conjunto de sentenças a partir da sucessiva derivação de produções
- Identificar possível linguagem da gramática

![Funcionamento](https://cloud.githubusercontent.com/assets/830208/10746319/b3a4a348-7c30-11e5-9146-8c5f944854b3.png)

## Como executar
Para executar o programa, é necessário ter o Python 2.7+ instalado no computador. A versão 3+ não é suportada.

Dentro do diretório do projeto executar `python -B mgaf.py`

## Testes automatizados
Dentro do diretório do projeto executar `python -B -m tests -v`
