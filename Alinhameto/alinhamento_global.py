data = open("Configuracoes.txt", "r").read()
data = data.replace(" ", "")
config = dict(item.split('=') for item in data.split())
fita_horizontal = config['fita_horizontal']
fita_vertical = config['fita_vertical']
match = int(config['match'])
mismatch = int(config['mismatch'])
gap = int(config['gap'])

print("Alinhamento Global - Smith-Waterman")
print("By: Gabriel Araújo Gonçalves\n")
print("Sequencia 1: ", fita_horizontal)
print("Sequencia 2: ", fita_vertical)
print("")


fita_vertical = "X" + fita_vertical
fita_horizontal = "X" + fita_horizontal
linhas = len(fita_vertical)
colunas = len(fita_horizontal)
def print_fitas_alinhadas(rota):
    fita_2 = ""
    fita_1 = ""
    for i in range(len(rota) -1 ):
        if (rota[i][0] == rota[i+1][0]+1) and (rota[i][1] == rota[i+1][1]+1):
            fita_1 = fita_horizontal[rota[i][1]] + fita_1
            fita_2 = fita_vertical[rota[i][0]] + fita_2
        elif(rota[i][0] == rota[i+1][0]+1):
            fita_1 = "-" + fita_1
            fita_2 = fita_vertical[rota[i][0]] + fita_2
        elif(rota[i][1] == rota[i+1][1]+1):
            fita_1 = fita_horizontal[rota[i][1]] + fita_1
            fita_2 = "-" + fita_2
    print("h: " + fita_1)
    print("v: " + fita_2)


def criar_matriz():
    matriz = [[{'valor': 0,'anterior': []} for coluna in fita_horizontal] for linha in fita_vertical]
    aux = 0

    for coluna in range(colunas):
        matriz[0][coluna]['valor'] = aux
        matriz[0][coluna]['anterior'].append([0,0])
        aux += gap
    aux = 0
    for linha in range(linhas):
        matriz[linha][0]['valor'] = aux
        matriz[linha][0]['anterior'].append([0,0])
        aux += gap
    return matriz


def funcao_match_mismatch(l,c):
    if fita_vertical[l] == fita_horizontal[c]:
        return match
    return mismatch

def encontrar_inicio_backtrace(matriz):
    aux = matriz[-1][-1]['valor']
    inicio = []
    for l in range(linhas):
        if matriz[l][-1]['valor'] >= aux:
            aux = matriz[l][-1]['valor']
    for l in range(linhas):
        if matriz[l][-1]['valor'] == aux:
            inicio.append([l,colunas-1])
    return inicio

def backtrace(matriz, l, c):
    rota = [[l, c]]
    score = matriz[l][c]['valor']
    print("Score: " + str(score))
    while(matriz[l][c]['anterior'][0] != [0, 0] ):
        lista_anteriores = matriz[l][c]['anterior']
        valor_max = matriz[lista_anteriores[0][0]][lista_anteriores[0][1]]['valor']
        for i in lista_anteriores:
            if valor_max <= matriz[i[0]][i[1]]['valor']:
                valor_max = matriz[i[0]][i[1]]['valor']
                l = i[0]
                c = i[1]
        rota.append([l, c])
        score += valor_max
    else:
        score += matriz[0][0]['valor']
        rota.append([0,0])
    #print("Score: " + str(score))
    return rota 

def criar_matriz_score(matriz):
    for l in range(linhas):
        for c in range(colunas):
            if l != 0 and c != 0:
                esquerda = matriz[l][c-1]['valor'] + gap
                baixo = matriz[l-1][c]['valor'] + gap
                diagornal = matriz[l-1][c-1]['valor'] + funcao_match_mismatch(l,c)
                maxi = max(esquerda, baixo, diagornal)
                matriz[l][c]['valor'] = maxi
                if(esquerda == maxi):
                    matriz[l][c]['anterior'].append([l,c-1])
                if(baixo == maxi):
                    matriz[l][c]['anterior'].append([l-1,c])
                if(diagornal == maxi):
                    matriz[l][c]['anterior'].append([l-1,c-1])


matriz = criar_matriz()
criar_matriz_score(matriz)

inicio_backtrace = encontrar_inicio_backtrace(matriz)
resposta = backtrace(matriz, inicio_backtrace[0][0], inicio_backtrace[0][1])
print_fitas_alinhadas(resposta)
print("Obs: para mudar os parâmetros configure o arquivo \"Configuracoes.txt\", se atentanto para o formato.")
