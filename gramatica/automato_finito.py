# -*- coding: utf-8 -*-
class AutomatoFinito:
    def __init__(self, linguagem):
        self.linguagem = linguagem

    def gerar(self):
        print 'Gerando o Automato a partir da linguagem: %s\n' % self.linguagem
        self.testar()
        if (self.linguagem[0] == 'L'):
            print 'Automato Tipo 1\n'
        else:
            print 'Automato Tipo 2\n'
            simbolos = self.linguagem.replace('{','').replace('}', '').split(',')

    def reconhecer(self, atual, sentenca, automato):
        print atual+' '+sentenca;
        if sentenca == '': 
            if atual in automato['fim']: 
                return True, atual 
            else:
                return False, atual
        if not atual in automato['regras']: return False, atual
        for x in automato['regras'][atual]:
            if x in automato['regras'][atual]: 
                if sentenca[0] in automato['regras'][atual][x]:
                    atual = x
                    sentenca = sentenca[1:]
                    saida = self.reconhecer(atual, sentenca, automato)
                    if saida[0]: return True, saida[1]
        return False, atual

    #sentecas devem estar no formato '{a,aab,baa,bab}'
    def gerar_por_sentencas(self, sentencas):
        
        #criando a estrutura do AF
        estados = ['q0']
        simbolos = []
        regras = {'q0':{'q0':''}}
        inicio = 'q0'
        fim = []

        #colocando os simbolos das sentencas na lista de simbolos
        sen = sentencas.replace('{','').replace('}', '').split(',')
        for x in sen : 
            x = x.strip()
            for c in x:
                if not c in simbolos: simbolos.append(c)

        automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}

        cont_estado = 0

        for s in sen:
            sentenca = s
            atual = 'q0'
            while len(sentenca)>0:
                saida = self.reconhecer('q0', sentenca, automato)
                if saida[0]:
                    atual = saida[1]
                    fim.append(atual)
                    # ???
                    automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
                    return automato
                cont_estado += 1
                novo = 'q'+cont_estado
                estados.append(novo)
                #ToDo - Criar uma função que adiciona um novo estados nas regras
                #ToDo - O estado atual apontando pro estado novo, adiciona senteca[0]
                sentenca = sentenca[1:]
                atual = novo
                if len(sentenca)==0: fim.append(novo)



    #linguagem deve estar no formato 'L=(a^m, b^n| m>=0, n=1)'
    def gerar_por_linguagens(self, linguagem):
        return None
            
    def testar(self):
        #exemplo de estrutura de um automato
        estados = ['q0', 'q1', 'q2']
        simbolos = ['a', 'b', 'c']
        regras = {'q0':{'q0':'b', 'q1':'a'}, 'q1':{'q2':'ab'}}
        inicio = 'q0'
        fim = ['q2']

        automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
        sentenca = 'bbbbbbbaab'

        saida = self.reconhecer('q0', sentenca, automato)
        if saida[0]:
            print 'Reconheceu: '+saida[1]
        else:
            print 'Nao Reconheceu: '+saida[1]


