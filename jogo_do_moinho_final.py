# Jiqi Wang 99241
def vitoria(t, peca):
    # vitoria: tabuleiro x peca -> str
    ''' Esta funcao recebe um tabuleiro e uma peca do jogador, 
e devolve uma posicao em string. 
Se o jogador tiver duas das suas pecas em linha/coluna e uma posicao livre 
entao marca na posicao livre, ganhando o jogo.'''
    posicoes_livres = obter_posicoes_livres(t)
    for pos in posicoes_livres:
        componente_c = posicao_para_str(pos)[0]
        componente_l = posicao_para_str(pos)[1]
        for vetor in ((obter_vetor(t, componente_c), \
                       obter_vetor(t, componente_l))):
            if sum([peca_para_inteiro(x) for x in vetor]) == \
               2 * peca_para_inteiro(peca):
# se a soma dentro de uma linha/coluna for 2*d, ou seja, 
# se tiver duas pecas nessa linha/coluna entao marca essa posicao
                return posicao_para_str(pos)


def bloqueio(t, peca):
    # bloqueio: tabuleiro x peca -> str
    ''' Esta funcao recebe um tabuleiro e uma peca do jogador,
e devolve uma posicao em string.
Se o adversario tiver duas das suas pecas em linha/coluna e uma posicao livre 
entao marca na posicao livre, bloqueando o adversario.'''
    peca_str = peca_para_str(peca)
    peca_em_jogo_str = {'X':'O', 'O':'X'}[peca_str[1]]
    peca_em_jogo = cria_peca(peca_em_jogo_str)
    return vitoria(t, peca_em_jogo)


def centro(t, peca):
    # centro: tabuleiro x peca -> str
    ''' Esta funcao recebe um tabuleiro e uma peca do jogador,
e devolve a posicao central em string se esta estiver livre.'''
    if eh_posicao_livre(t, cria_posicao('b', '2')):
        return 'b2'


def canto_vazio(t, peca):
    # canto_vazio: tabuleiro x peca -> str
    ''' Esta funcao recebe um tabuleiro e uma peca do jogador,
e devolve o canto vazio de menor posicao que estiver livre em string.'''
    tuplo = (cria_posicao('a', '1'), cria_posicao('c', '1'),
             cria_posicao('a', '3'), cria_posicao('c', '3'))
    for i in tuplo:
        if eh_posicao_livre(t, i):
            return posicao_para_str(i)


def lateral_vazio(t, peca):
    # lateral_vazio: tabuleiro x peca -> str
    ''' Esta funcao recebe um tabuleiro e uma peca do jogador, 
e devolve o lateral vazio de menor posicao que estiver livre em string.'''
    tuplo = (cria_posicao('b', '1'), cria_posicao('a', '2'),
             cria_posicao('c', '2'), cria_posicao('b', '3'))
    for i in tuplo:
        if eh_posicao_livre(t, i):
            return posicao_para_str(i)




# TAD POSICAO: Representa uma posicao do tabuleiro em jogo. 
# Representacao interna: tuplo constituida por duas strings (c,l)
# cria_posicao: str x str -> posicao
# cria_copia_posicao: posicao -> posicao
# obter_pos_c: posicao -> str
# obter_pos_l: posicao -> str
# eh_posicao: universal -> booleano
# posicoes_iguais: posicao x posicao -> booleano
# posicao_para_str: posicao -> str

def cria_posicao(c, l):
    # cria_posicao: str x str -> posicao
    ''' Esta funcao recebe duas cadeias de carateres (coluna - c, linha - l) 
de uma posicao e devolve a posicao correspondente. '''
    if c == 'a' or c == 'b' or c == 'c':
        if l == '1' or l == '2' or l == '3':
            return (c, l)
    raise ValueError('cria_posicao: argumentos invalidos')


def cria_copia_posicao(pos):
    # cria_copia_posicao: posicao -> posicao
    ''' Esta funcao recebe uma posicao e devolve uma copia nova da posicao.'''
    if not cria_posicao(pos[0], pos[1]):
        raise ValueError('cria_copia_posicao: argumentos invalidos')
    return (pos[0], pos[1])


def obter_pos_c(pos):
    # obter_pos_c: posicao -> str
    ''' Esta funcao recebe uma posicao e devolve a componente coluna c 
da posicao.'''
    return pos[0]


def obter_pos_l(pos):
    # obter_pos_l: posicao -> str
    ''' Esta funcao recebe uma posicao e devolve a componente linha l 
da posicao.'''
    return pos[1]


def eh_posicao(arg):
    # eh_posicao: universal -> booleano
    ''' Esta funcao recebe um argumento 
e verifica se corresponde a uma posicao do tabuleiro.'''  
    if not isinstance(arg, tuple) or len(arg) != 2:
        return False
    if arg[0] == 'a' or arg[0] == 'b' or arg[0] == 'c':
        if arg[1] == '1' or arg[1] == '2' or arg[1] == '3':
            return True
    return False


def posicoes_iguais(pos1, pos2):
    # posicoes_iguais: posicao x posicao -> booleano
    ''' Esta funcao recebe duas posicoes e verifica se sao posicoes iguais.'''  
    return pos1 == pos2


def posicao_para_str(pos):
    # posicao_para_str: posicao -> str
    ''' Esta funcao recebe uma posicao e devolve a cadeia de caracteres ‘cl’, 
sendo os valores c e l as componentes coluna e linha.''' 
    return str(pos[0] + pos[1])


def obter_posicoes_adjacentes(pos):
    # obter_posicoes_adjacentes: posicao -> tuplo de posicoes
    ''' Esta funcao recebe uma posicao e devolve um tuplo com as posicoes 
adjacentes a posicao de acordo com a ordem de leitura do tabuleiro.'''
    tuplo_posicoes = ()
    c = ord(obter_pos_c(pos))
    l = int(obter_pos_l(pos))
    if l != 1: #linhas 2 e 3
        if c == 98 and l == 2 or c == 99 and l == 3: # b2,c3
            tuplo_posicoes += (cria_posicao(chr(c - 1), str(l - 1)), )
            # cima esquerda: b2 -> a1, c3 -> b2
        tuplo_posicoes += (cria_posicao(chr(c), str(l - 1)), ) # cima
        if c == 98 and l == 2 or c == 97 and l == 3: # b2, a3
            tuplo_posicoes += (cria_posicao(chr(c + 1), str(l - 1)), )
            # cima direita: b2 -> c1, a3 -> b2
    if c != 97: # colunas b e c
        tuplo_posicoes += (cria_posicao(chr(c - 1), str(l)), ) # esquerda
    if c != 99: # colunas a e b
        tuplo_posicoes += (cria_posicao(chr(c + 1), str(l)), ) # direita
    if l != 3: # linhas 1 e 2
        if c == 98 and l == 2 or c == 99 and l == 1: # b2, c1
            tuplo_posicoes += (cria_posicao(chr(c - 1), str(l + 1)), )
            #baixo esquerda: b2 -> a3, c1 -> b2
        tuplo_posicoes += (cria_posicao(chr(c), str(l + 1)), ) # baixo
        if c == 98 and l == 2 or c == 97 and l == 1: # b2, a1
            tuplo_posicoes += (cria_posicao(chr(c + 1), str(l + 1)), )
            # baixo direita: b2 -> c3, a1 -> b2
    return tuplo_posicoes




# TAD PECA: Representa as pecas do jogo.
# Representacao interna: lista de um elemento ([X], [O] ou [ ])
# cria_peca: str -> peca
# cria_copia_peca: peca -> peca
# eh_peca: universal -> booleano
# pecas_iguais: peca x peca -> booleano
# peca_para_str: peca -> str

def cria_peca(s):
    # cria_peca: str -> peca
    ''' Esta funcao recebe uma cadeia de carateres correspondente ao 
identificador de um dos dois jogadores ('X' ou 'O') ou a uma peca livre (' ') 
e devolve a peca correspondente.''' 
    if not isinstance(s, str):
        raise ValueError('cria_peca: argumento invalido')
    if s != 'X' and s != 'O' and s != ' ':
        raise ValueError('cria_peca: argumento invalido')
    return [s]


def cria_copia_peca(peca):
    # cria_copia_peca: peca -> peca
    ''' Esta funcao recebe uma peca do jogador 
e devolve uma copia nova da peca.'''
    if not cria_peca(peca[0]):
        raise ValueError('cria_copia_peca: argumento invalido')
    return cria_peca(peca[0])


def eh_peca(arg):
    # eh_peca: universal -> booleano
    ''' Esta funcao recebe um argumento 
e verifica se corresponde a uma peca do tabuleiro.'''  
    if not isinstance(arg, list) or len(arg) != 1:
        return False
    if arg[0] == 'X' or arg[0] == 'O' or arg[0] == ' ':
        return True
    return False


def pecas_iguais(peca1, peca2):
    # pecas_iguais: peca x peca -> booleano
    ''' Esta funcao recebe duas pecas e verifica se sao pecas iguais.''' 
    if not eh_peca(peca1) or not eh_peca(peca2):
        return False
    return peca1[0] == peca2[0]


def peca_para_str(peca):
    # peca_para_str: peca -> str
    ''' Esta funcao recebe uma peca do jogador e devolve a cadeia de caracteres
que representa o jogador dono da peca, isto e, '[X]', '[O]' ou '[ ]'.''' 
    return '[' + peca[0] + ']'


def peca_para_inteiro(peca):
    # peca_para_inteiro: peca -> N
    ''' Esta funcao recebe uma peca do jogador e devolve um inteiro valor 
1, -1 ou 0, dependendo se a peca for do jogador 'X', 'O' 
ou livre, respetivamente.'''
    x = peca_para_str(peca)
    if x[1] == 'X':
        return 1
    if x[1] == 'O':
        return -1
    if x[1] == ' ':
        return 0


# TAD TABULEIRO: Representa um tabuleiro do jogo do moinho
# Representacao interna: dicionario (key - string; value - lista)
# cria_tabuleiro: {} -> tabuleiro
# cria_copia_tabuleiro: tabuleiro -> tabuleiro
# obter_peca: tabuleiro x posicao -> peca
# tabuleiro x str -> tuplo de pecas
# coloca_peca: tabuleiro x peca x posicao -> tabuleiro
# remove_peca: tabuleiro x posicao -> tabuleiro
# move_peca: tabuleiro x posicao x posicao -> tabuleiro
# eh_tabuleiro: universal -> booleano
# eh_posicao_livre: tabuleiro x posicao -> booleano
# tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
# tabuleiro_para_str: tabuleiro -> str
# tuplo_para_tabuleiro: tuplo -> tabuleiro

def cria_tabuleiro():
    # cria_tabuleiro: {} -> tabuleiro
    ''' Esta funcao devolve um tabuleiro de jogo do moinho de 3x3 
sem posicoes ocupadas por pecas de jogador.'''
    d = { 'a1': [' '], 'b1': [' '], 'c1': [' '], 'a2': [' '], 'b2': [' '], \
          'c2': [' '], 'a3': [' '], 'b3': [' '], 'c3': [' '],}
    return d


def cria_copia_tabuleiro(t):
    # cria_copia_tabuleiro: tabuleiro -> tabuleiro
    ''' Esta funcao recebe um tabuleiro e devolve 
uma copia nova do tabuleiro.'''
    if not eh_tabuleiro(t):
        raise ValueError('cria_copia_tabuleiro: argumento invalido')
    return t.copy()


def obter_peca(t, pos):
    # obter_peca: tabuleiro x posicao -> peca
    ''' Esta funcao recebe um tabuleiro e uma posicao, e devolve a peca do
jogador na posicao do tabuleiro. 
Se a posicao nao estiver ocupada, devolve uma peca livre.'''
    p = posicao_para_str(pos)
    peca = t.get(p)
    return cria_peca(peca[0])


def obter_vetor(t, s):
    # tabuleiro x str -> tuplo de pecas
    ''' Esta funcao recebe um tabuleiro e uma cadeia de caracteres, e devolve 
todas as pecas da linha ou coluna especificada pelo seu argumento.'''
    # s='a','1',...
    tuplo = ()
    sorted_keys = [ 'a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
    for i in sorted_keys:
        if s in i:
            tuplo += (cria_peca(t[i][0]), ) 
    return tuplo


def coloca_peca(t, peca, pos):
    # coloca_peca: tabuleiro x peca x posicao -> tabuleiro
    ''' Esta funcao recebe um tabuleiro, uma peca do jogador e uma posicao.
Modifica destrutivamente o tabuleiro, colocando a peca indicada 
na posicao pretendida, e devolve o proprio tabuleiro.'''
    pos_str = posicao_para_str(pos)
    peca_str = peca_para_str(peca)
    t.update({pos_str: [peca_str[1]]})
    return t


def remove_peca(t, pos):
    # remove_peca: tabuleiro x posicao -> tabuleiro
    ''' Esta funcao recebe um tabuleiro, uma peca e uma posicao.
Modifica destrutivamente o tabuleiro, removendo a peca da posicao indicada, 
e devolve o proprio tabuleiro.'''
    p = posicao_para_str(pos)
    t.update({p: [' ']})
    return t


def move_peca(t, pos1, pos2):
    # move_peca: tabuleiro x posicao x posicao -> tabuleiro
    ''' Esta funcao recebe um tabuleiro, uma posicao1 e uma posicao2.
Modifica destrutivamente o tabuleiro, movendo a peca que encontra na posicao1 
para a posicao2, e devolve o proprio tabuleiro.'''
    peca1 = obter_peca(t, pos1)
    remove_peca(t, pos1)
    coloca_peca(t, peca1, pos2)
    return t


def obter_vetor1(t, s):
    # obter_vetor_sem_abstracao_em_peca
    return tuple(value for (key, value) in t.items() if s in key)


def eh_tabuleiro(arg):
    # eh_tabuleiro: universal -> booleano
    ''' Esta funcao recebe um argumento 
e verifica se corresponde a um tabuleiro.'''
    if not isinstance(arg, dict):
        return False
    pecasX = sum(value == ['X'] for value in arg.values())
    pecasO = sum(value == ['O'] for value in arg.values())
    if pecasX > 3 or pecasO > 3 or abs(pecasX - pecasO) > 1:
        return False
    for i in range(1, 4):
        for j in range(i, 4):
            if obter_vetor1(arg, str(i)) == (['X'], ['X'], ['X']) \
                and obter_vetor1(arg, str(j)) == (['O'], ['O'], ['O']):
                return False
            if obter_vetor1(arg, str(i)) == (['O'], ['O'], ['O']) \
                and obter_vetor1(arg, str(j)) == (['X'], ['X'], ['X']):
                return False
    for k in range(97, 100):
        for l in range(k, 100):
            if obter_vetor1(arg, chr(k)) == (['X'], ['X'], ['X']) \
                and obter_vetor1(arg, chr(l)) == (['O'], ['O'], ['O']):
                return False
            if obter_vetor1(arg, chr(k)) == (['O'], ['O'], ['O']) \
                and obter_vetor1(arg, chr(l)) == (['X'], ['X'], ['X']):
                return False
    return True


def eh_posicao_livre(t, pos):
    # eh_posicao_livre: tabuleiro x posicao -> booleano
    ''' Esta funcao recebe um tabuleiro e uma posicao, 
e verifica se a posicao corresponde a uma posicao livre do tabuleiro.'''
    p = posicao_para_str(pos)
    for (key, value) in t.items():
        if p == key and value == [' ']:
            return True
    return False


def tabuleiros_iguais(t1, t2):
    # tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    ''' Esta funcao recebe dois tabuleiros e verifica se sao iguais.''' 
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def tabuleiro_para_str(t):
    # tabuleiro_para_str: tabuleiro -> str
    ''' Esta funcao recebe um tabuleiro e devolve a cadeia de caracteres que 
corresponde a representacao textual do tabuleiro.''' 
    stringlist = []
    stringlist.append('   a   b   c\n')
    for l in range(1, 4):  # linhas 1 2 3
        stringlist.append(str(l) + ' ')
        linhatabuleiro = obter_vetor(t, str(l))
        for c in range(0, 3):  # iterar na linhatabuleiro (lista)
            stringlist.append(peca_para_str(linhatabuleiro[c]))
            if c != 2:
                stringlist.append('-')
        if l == 1:
            stringlist.append('\n   | \ | / |\n')
        if l == 2:
            stringlist.append('\n   | / | \ |\n')
    return ''.join(stringlist)


def tuplo_para_tabuleiro(t):
    # tuplo_para_tabuleiro: tuplo -> tabuleiro
    ''' Esta funcao recebe um tuplo com 3 tuplos, cada um deles contendo 
3 valores inteiros (1, -1 ou 0), e devolve o tabuleiro correspondente.'''
    tabuleiro = {}
    for v in range(0, 3):
        for i in range(0, 3):
            peca = {1: ['X'], -1: ['O'], 0: [' ']}[t[v][i]]
            tabuleiro[chr(i + 97) + str(v + 1)] = peca
            # chr(0+97)+str(0+1)='a','1';chr(1+97)+str(1)='b','1'
            # tabuleiro de esquerda para a direita e de cima para baixo
    return tabuleiro


def obter_ganhador(t):
    # obter_ganhador: tabuleiro -> peca
    ''' Esta funcao recebe um tabuleiro e devolve uma peca do jogador 
que tenha as suas 3 pecas em linha (vertical ou horizontal) no tabuleiro. 
Se nao existir nenhum ganhador, devolve uma peca livre.'''
    for l in range(1, 4):  # 1,2,3
        soma = 0
        for peca in obter_vetor(t, str(l)):
            soma += peca_para_inteiro(peca)
        if soma == 3:
            return cria_peca('X')
        if soma == -3:
            return cria_peca('O')
    for c in range(97, 100):  # a,b,c
        soma = 0
        for peca1 in obter_vetor(t, chr(c)):
            soma += peca_para_inteiro(peca1)
        if soma == 3:
            return cria_peca('X')
        if soma == -3:
            return cria_peca('O')
    return cria_peca(' ')


def obter_posicoes_livres(t):
    # obter_posicoes_livres: tabuleiro -> tuplo de posicoes
    ''' Esta funcao recebe um tabuleiro e devolve um tuplo ordenado com todas 
as posicoes livres do tabuleiro.'''
    tuplo = ()
    for l in range(1, 4): # 1,2,3
        tuplo_pecas = obter_vetor(t, str(l))
        for i in range (len(tuplo_pecas)): 
            if peca_para_inteiro(tuplo_pecas[i]) == 0:
                tuplo += (cria_posicao(chr(i+97), str(l)),)
    return tuplo



def obter_posicoes_jogador(t, peca):
    # obter_posicoes_jogador: tabuleiro x peca -> tuplo de posicoes
    ''' Esta funcao recebe um tabuleiro e uma peca de um jogador, e devolve 
um tuplo ordenado com todas as posicoes ocupadas pela 
peca do jogador indicado.'''
    tuplo = ()
    for l in range(1, 4):
        tuplo_pecas = obter_vetor(t, str(l))
        for i in range (len(tuplo_pecas)):
            if peca_para_inteiro(tuplo_pecas[i]) == peca_para_inteiro(peca):
                tuplo += (cria_posicao(chr(i+97), str(l)),)          
    return tuplo



def obter_movimento_manual(t, peca):
    # obter_movimento_manual: tabuleiro x peca -> tuplo de posicoes
    ''' Esta funcao recebe um tabuleiro e uma peca de um jogador, e devolve um
tuplo com uma ou duas posicoes que representam uma posicao ou um movimento 
introduzido manualmente pelo jogador. '''
    pecasP = len(obter_posicoes_jogador(t, peca))
    movimento = ()
    if pecasP < 3: # fase de colocacao
        x = input('Turno do jogador. Escolha uma posicao: ')
        if len(x) != 2 or (x[0] != 'a' and x[0] != 'b' and x[0] != 'c') or \
            (x[1] != '1' and x[1] != '2' and x[1] != '3'):
            raise ValueError('obter_movimento_manual: escolha invalida')
        pos = cria_posicao(x[0], x[1])
        if not eh_posicao_livre(t, pos):
            raise ValueError('obter_movimento_manual: escolha invalida')
        movimento += (pos, )
    if pecasP == 3: # fase de movimento
        x = input('Turno do jogador. Escolha um movimento: ')
        if len(x) != 4 or (x[0] != 'a' and x[0] != 'b' and x[0] != 'c') or \
            (x[1] != '1' and x[1] != '2' and x[1] != '3') or (x[2] != 'a' and\
             x[2] != 'b' and x[2] != 'c') or (x[3] != '1' and x[3] != '2' and\
             x[3] != '3'):
            raise ValueError('obter_movimento_manual: escolha invalida')
        pos = cria_posicao(x[0], x[1])
        peca_em_posicao_inicial = obter_peca(t, pos)
        if not pecas_iguais(peca, peca_em_posicao_inicial):
            raise ValueError('obter_movimento_manual: escolha invalida')
        pos1 = cria_posicao(x[2], x[3])
        posicoes_jogador = obter_posicoes_jogador(t, peca)
        todos_ocupados = True
        for posicoes in posicoes_jogador:
            for posicoes_adjacentes in \
                obter_posicoes_adjacentes(posicoes):
                if eh_posicao_livre(t, posicoes_adjacentes):
                    todos_ocupados = False
        if not todos_ocupados:
            if not eh_posicao_livre(t, pos1):
                raise ValueError('obter_movimento_manual: escolha invalida')
            if all( not posicoes_iguais(pos1, pos_adj) for pos_adj in \
                obter_posicoes_adjacentes(pos)):
                raise ValueError('obter_movimento_manual: escolha invalida')
        else: #se estiver bloqueado
            if not eh_posicao_livre(t, pos1) \
                and not posicoes_iguais(pos, pos1):
                raise ValueError('obter_movimento_manual: escolha invalida')
        movimento += (pos, pos1)
    return movimento



def obter_movimento_auto(t, peca, dificuldade):
    # obter_movimento_auto: tabuleiro x peca x str -> tuplo de posicoes
    ''' Esta funcao recebe um tabuleiro e uma peca de um jogador e uma cadeia
de caracteres representando o nivel de dificuldade, e devolve um
tuplo com uma ou duas posicoes que representam uma posicao ou um movimento 
escolhido automaticamente. '''
    pecasP = len(obter_posicoes_jogador(t, peca))
    movimento = ()
    if pecasP < 3:
        criterios = (vitoria, bloqueio, centro, canto_vazio, lateral_vazio)
        for criterio in criterios:
            if criterio(t, peca) is not None:
                posicao_str = criterio(t, peca)
                pos = cria_posicao(posicao_str[0], posicao_str[1])
                break
        movimento += (pos, )
    if pecasP == 3:
        if dificuldade == 'facil':
            for posicao_inicial in obter_posicoes_jogador(t, peca):
                for posicao_adjacente in \
                    obter_posicoes_adjacentes(posicao_inicial):
                    for posicao_livre in obter_posicoes_livres(t):
                        if posicoes_iguais(posicao_livre, posicao_adjacente):
                            return (posicao_inicial, posicao_adjacente)
        if dificuldade == 'normal':
            movimento = minimax(t, peca, 1, ())[1][0]
        if dificuldade == 'dificil':
            movimento = minimax(t, peca, 5, ())[1][0]
    return movimento



def minimax(tabuleiro, jogador, profundidade, seq_movimento): 
    # seq_movimento = tuplo de tuplos inicialmente vazio, jogador = str 'X' 'O'
    ganhador_peca = obter_ganhador(tabuleiro)
    melhor_seq_movimento = ()
    peca_str = peca_para_str(jogador)
    melhor_resultado = {'[X]': -1, '[O]': 1}[peca_str]
    if not pecas_iguais(ganhador_peca, cria_peca(' ')) or profundidade == 0:
        return (peca_para_inteiro(ganhador_peca), seq_movimento)
    else:
        for posicao_com_peca in obter_posicoes_jogador(tabuleiro,jogador):
            for posicao_adjacente_de_peca in \
                obter_posicoes_adjacentes(posicao_com_peca):
                if eh_posicao_livre(tabuleiro, posicao_adjacente_de_peca):
                    tabuleiro_novo = cria_copia_tabuleiro(tabuleiro)
                    move_peca(tabuleiro_novo, posicao_com_peca, \
                    posicao_adjacente_de_peca)
                    novo_movimento = (posicao_com_peca,\
                                      posicao_adjacente_de_peca)
                    outro_jogador_str = { '[X]': 'O','[O]': 'X'}[peca_str]
                    outro_jogador = cria_peca(outro_jogador_str)
                    novo_resultado = minimax(tabuleiro_novo,  outro_jogador, \
                            profundidade-1, seq_movimento + (novo_movimento,))
                    if melhor_seq_movimento == () or ( pecas_iguais(jogador, \
                    cria_peca('X')) and novo_resultado[0] > melhor_resultado)\
                    or (pecas_iguais(jogador, cria_peca('O')) and \
                    novo_resultado[0] < melhor_resultado):
                        melhor_resultado = novo_resultado[0]
                        melhor_seq_movimento = novo_resultado[1]
        return (melhor_resultado, melhor_seq_movimento)



def moinho(jogador,dificuldade):
    # moinho: str x str -> str
    ''' Esta funcao recebe duas cadeias de caracteres, a primeira 
corresponde a peca do jogador humano e a segunda o nivel de dificuldade 
e devolve a representacao externa da peca ganhadora ('[X]' ou '[O]'). '''
    if (jogador != '[X]' and jogador != '[O]') or \
        (dificuldade!='facil' and dificuldade!='normal' \
         and dificuldade!='dificil'):
        raise ValueError('moinho: algum dos argumentos e invalido.')
    
    print('Bem-vindo ao JOGO DO MOINHO. \
Nivel de dificuldade '+dificuldade+'.')
    Turno_do_jogador = True if jogador == '[X]' else False
    t = cria_tabuleiro()
    print(tabuleiro_para_str(t))
    peca_jogador = cria_peca(jogador[1])
    outro_jogador_str = { '[X]': 'O','[O]': 'X'}[peca_para_str(peca_jogador)]
    outro_jogador = cria_peca(outro_jogador_str)
    while pecas_iguais(obter_ganhador(t),  cria_peca(' ')):
        if Turno_do_jogador: 
            posicao_escolhida = obter_movimento_manual(t, peca_jogador)
            if len(posicao_escolhida) == 1:
                coloca_peca(t, peca_jogador, posicao_escolhida[0])
            else:
                move_peca(t, posicao_escolhida[0], posicao_escolhida[1])
            print(tabuleiro_para_str(t))
        else: 
            print("Turno do computador ("+dificuldade+"):")
            posicao_escolhida = \
                obter_movimento_auto(t, outro_jogador, dificuldade)
            if len(posicao_escolhida) == 1:
                coloca_peca(t, outro_jogador, posicao_escolhida[0])
            else:
                move_peca(t, posicao_escolhida[0], posicao_escolhida[1])
            print(tabuleiro_para_str(t))
        Turno_do_jogador = not Turno_do_jogador 
    return peca_para_str(obter_ganhador(t))
  