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
        for x in automato['regras'][atual]:
            if sentenca[0] in automato['regras'][atual][x]:
                atual = x
                sentenca = sentenca[1:];
                saida = self.reconhecer(atual, sentenca, automato)
                if saida[0]: return True, saida[1]
        return False, atual

            
    def testar(self):
        #exemplo de estrutura de um automato
        estados = ['q0', 'q1', 'q2']
        simbolos = ['a', 'b', 'c']
        regras = {'q0':{'q0':'b', 'q1':'a', 'q2':''}, 'q1':{'q0': '', 'q1':'', 'q2':'ab'}, 'q2':{'q0':'', 'q1':'', 'q2':''}}
        inicio = 'q0'
        fim = ['q2']

        automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
        sentenca = 'bbbbbbbaa'

        saida = self.reconhecer('q0', sentenca, automato)
        if saida[0]:
            print 'Reconheceu: '+saida[1]
        else:
            print 'Nao Reconheceu: '+saida[1]


