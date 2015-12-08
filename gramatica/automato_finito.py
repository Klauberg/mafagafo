# -*- coding: utf-8 -*-
class AutomatoFinito:
    def __init__(self, linguagem, sentencas):
        self.linguagem = linguagem
        self.sentencas = sentencas

    def gerar(self):
        aut = self.gerar_por_sentencas(self.sentencas)
        self.imprimir_automato(aut)
        if self.automato_finito_deterministico(aut):
            print '\nO Automato Finito é Determinístico\n'
        else: 
            print '\nO Automato Finito é Não-Determinístico\n'
        aux = self.sentencas.replace('{','').replace('}','').split(',')
        for s in aux:
            if self.reconhecer('q0', s, aut)[0]:
                print s+': Reconhecida'
            else:
                print s+': Não Reconhecida'

    def reconhecer(self, estado_atual, sentenca, automato):
        sentenca = sentenca.strip()
        if sentenca == '': 
            if estado_atual in automato['fim']: 
                return True, estado_atual 
            else:
                return False, estado_atual
        if not estado_atual in automato['regras']: return False, estado_atual
        for x in automato['regras'][estado_atual]:
            if x in automato['regras'][estado_atual] and len(sentenca)>0:
                if sentenca[0] in automato['regras'][estado_atual][x]:
                    estado_atual = x
                    sentenca = sentenca[1:]
                    saida = self.reconhecer(estado_atual, sentenca, automato)
                    if saida[0]: return True, saida[1]
        return False, estado_atual

    #retorna verdadeiro se o automato for determinístico, caso contrário ele é não determinístico
    def automato_finito_deterministico(self, automato):
        for r in automato['regras']:
            simbolos = []
            for e in automato['regras'][r]:
                if automato['regras'][r][e] != '':
                    if automato['regras'][r][e] in simbolos:
                        return False
                    else:
                        simbolos.append(automato['regras'][r][e])

        return True


    def imprimir_automato(self, automato):
        estados = ''
        for e in automato['estados']: estados+=', '+e
        estados=estados[2:]
        estados = '('+estados+')'

        simbolos = ''
        for s in automato['simbolos']: simbolos+=', '+s
        simbolos=simbolos[2:]
        simbolos = '('+simbolos+')'

        inicio = automato['inicio']

        fim = ''
        for s in automato['fim']: fim+=', '+s
        fim=fim[2:]
        fim = '('+fim+')'
        print '\nAutômato Finito:'
        print 'M = {'+estados+', '+simbolos+', R, '+inicio+', '+fim+'}\n'

        linha = '+-------+'
        for s in automato['simbolos']: linha+='--------------------+'
        print linha
        linha = '|   R   |'
        for s in automato['simbolos']: linha+='         '+s+'          |'
        print linha
        linha = '+-------+'
        for s in automato['simbolos']: linha+='--------------------+'
        print linha

        #imprimir tabela
        for e in automato['estados']:
            linha = '|'
            if e in automato['inicio']:
                linha+='->'
            else:
                linha+='  '
            if len(e) == 2:
                linha+=' '+e
            else:
                linha+=e
            if e in automato['fim']:
                linha+='* |'
            else:
                linha+='  |'
            for s in automato['simbolos']:
                coluna = 20
                if not e in automato['regras']:
                    linha+='                    |'
                else:
                    primeiro = True
                    for q in automato['regras'][e]:
                        if s in automato ['regras'][e][q]:
                            if primeiro:    
                                linha+='{'+q
                                primeiro = False
                                coluna+=1
                            else:
                                linha+=', '+q
                            if len(q) == 2:
                                coluna-=4
                            else:
                                coluna-=5
                    if primeiro:
                        linha+='                    |'
                    else:
                        linha+='}'
                        for x in xrange(0,coluna-1):
                            linha+=' '
                        linha+='|'

            print linha
        linha = '+-------+'
        for s in automato['simbolos']: linha+='--------------------+'
        print linha

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
        
        for sentenca in sen:
            s = sentenca.strip()
            estado_atual = inicio
            while (len(s)>0):
                # Se a sentença já consegue ser reconhecida pelo AF, então pulo pra próxima
                if not self.reconhecer('q0', sentenca, automato)[0]:
                    #Verifico se o estado atual tem uma ligação para o primeiro caractere da sentenca
                    tem = False
                    for r in regras[estado_atual]:
                        if sentenca[0] in regras[estado_atual][r]:
                            #se sim, vou para esse estado
                            estado_atual = r
                            if len(s) == 1:
                                #estado final
                                fim.append(estado_atual)
                                automato = {'estados':estados, 'simbolos':simbolos, 'regras':regras, 'inicio':inicio, 'fim':fim}
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



