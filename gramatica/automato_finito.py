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
            #teste
            sentencas_teste = '{aca, bcb, acb, ccb}'
            aut = self.gerar_por_sentencas(sentencas_teste)
            print aut

    def reconhecer(self, estado_atual, sentenca, automato):
        #print estado_atual+' '+sentenca;
        if sentenca == '': 
            if estado_atual in automato['fim']: 
                return True, estado_atual 
            else:
                return False, estado_atual
        if not estado_atual in automato['regras']: return False, estado_atual
        for x in automato['regras'][estado_atual]:
            if x in automato['regras'][estado_atual]: 
                if sentenca[0] in automato['regras'][estado_atual][x]:
                    estado_atual = x
                    sentenca = sentenca[1:]
                    saida = self.reconhecer(estado_atual, sentenca, automato)
                    if saida[0]: return True, saida[1]
        return False, estado_atual

    #sentecas devem estar no formato '{a,aab,baa,bab}'
    def gerar_por_sentencas(self, sentencas):
        
        #criando a estrutura do AF
        estados = ['q0']
        simbolos = []
        regras = {'q0':{}}
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
         #começo no estado inicial já definido

        limite = 20
        for sentenca in sen:
            
            s = sentenca.strip()
            estado_atual = inicio
            

            while (len(s)>0):

                if limite == 0: 
                    break 
                else: limite-=1

                # Se a sentença já consegue ser reconhecida pelo AF, então pulo pra próxima
                if not self.reconhecer('q0', sentenca, automato)[0]:
                    #Verifico se o estado atual tem uma ligação para o primeiro caractere da sentenca
                    tem = False
                    for r in regras[estado_atual]:
                        if sentenca[0] in regras[estado_atual][r]:
                            #se sim, vou para esse estado
                            estado_atual = r
                            s = s[1:]
                            tem = True
                            break

                    #se não tem ligação com o simbolo
                    if not tem:
                        #se não estou no ultimo símbolo da sentença e para todos os estados (menos o estado atual), 
                        #algum reconhece a sentenca sem o primeiro caractere, supondo que eles sejam o estado inicial
                        tem = False
                        for e in estados:
                            saida = self.reconhecer(e, s[1:], automato)
                            if saida[0]:
                                #se sim, crio uma ligação entre o estado atual e o estado encontrado com o primeiro caractere da sentenca
                                self.criar_ligacao_automato(regras, estado_atual, e, s[0])
                                automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
                                estado_atual = e
                                s = s[1:]
                                tem = True
                                break
                        if not tem:
                            cont_estado += 1
                            novo = 'q'+`cont_estado`
                            estados.append(novo)
                            if len(s) == 1:
                                #estado final
                                fim.append(novo)
                            self.criar_ligacao_automato(regras, estado_atual, novo, s[0])
                            regras.update({novo:{}})
                            automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
                            estado_atual = novo
                            s = s[1:]
                else:
                    'Mas entrou aki'
                    break
        return automato

    def criar_ligacao_automato(self, regras, origem, destino, simbolo):
        if not origem in regras:
            regras.update({origem:{}})

        if not destino in regras[origem]:
            regras[origem].update({destino:''})

        if not simbolo in regras[origem][destino]:
            regras[origem][destino] += simbolo




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


