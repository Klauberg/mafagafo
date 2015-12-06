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
        if sentenca == '': return atual
        acho = False
        for x in automato['regras'][atual]:
            if sentenca[0] in automato['regras'][atual][x]:
                acho = True
                atual = x
                sentenca = sentenca[1:];
                if self.reconhecer(atual, sentenca, automato) != '': return atual 
        if not acho:
            return ''

            
    def testar(self):
        #exemplo de estrutura de um automato
        estados = ['q0', 'q1', 'q2']
        simbolos = ['a', 'b', 'c']
        regras = {'q0':{'q0':'b', 'q1':'a'}, 'q1':{'q2':'ab'}}
        inicio = 'q0'
        fim = ['q2']

        automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
        sentenca = 'bbaa'

        saida = self.reconhecer('q0', sentenca, automato)
        print saida


