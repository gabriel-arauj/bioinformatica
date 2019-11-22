import sys



# Abrindo arquivo kdmer
def abrirArquivo():
    try:
        caminho = sys.argv[1]
    except:
        print("Passe o arquivo como arguemento na chamada do programa!" )
        exit()
    try:
        f = open(caminho, 'r')
    except:
        print("Arquivo não encontrado!!")
        exit()
    k, d= caminho.split("d")
    k = int(k.split('k')[1])
    d = int(d.split("mer.txt")[0])
    x = f.read()
    ls = x.replace('[', "").replace(']', "").replace('\'', "").replace(" ", "").split(',')
    return {'k':k,'d':d,'sequencia':ls}

def prefixo(i):
    s1 , s2 = i.split('|')
    s1 = s1[0:-1]
    s2 = s2[0:-1]
    return (s1, s2)

def sufixo(i):
    s1 , s2 = i.split('|')
    s1 = s1[1:]
    s2 = s2[1:]
    return (s1, s2)

def geraAdjLista(composicao):
    rotulo = {}
    grafo = {}
    saida = {}
    entrada = {}
    for x in composicao['sequencia']:
        pre = prefixo(x)
        suf = sufixo(x)
        rotulo[pre] = x
        grafo[pre] = []
        saida[pre] = 0
        saida[suf] = 0
        entrada[suf] = 0
        entrada[pre] = 0
    for x in composicao['sequencia']:
        pre = prefixo(x)
        suf = sufixo(x)
        grafo[pre].append(suf)
        saida[pre] += 1
        entrada[suf] += 1
    return [grafo,saida,entrada, rotulo]

def encontraInicio(entrada, saida):
    mim = 0
    chave = list(entrada)[0]
    for i in (entrada):
        if entrada[i] - saida[i] <= mim:
            mim = entrada[i] - saida[i]
            chave = i
    return chave

def acha_caminho(grafo, entrada, saida, chave):
    caminho = []
    pilha = []
    while True:
        if len(pilha) == 0 and saida[chave] == 0:
            caminho.append(chave)
            break
        else:
            if saida[chave] == 0:
                caminho.append(chave)
                chave = pilha.pop()
            else:
                pilha.append(chave)
                viz = grafo[chave].pop()
                saida[chave] +=-1
                entrada[viz] +=-1
                chave = viz
    return caminho[::-1]

def remonta( d, k, caminho, rotulo):
    sequencia = ""
    for i in caminho[:-1]:
        ini = i[0]
        if sequencia == "":
            sequencia += ini
        else:
            sequencia += ini[-1]
    tam = len(caminho)
    for i in range(d + 1):
        sequencia += caminho[tam-d + i -4][1][1]
        #print( caminho[tam-d + i -4][1][1])
    return sequencia + caminho[-2][1][0] + caminho[-1][1]


composicao = abrirArquivo()
grafo, saida, entrada, rotulo = geraAdjLista(composicao)
chave_inicio = encontraInicio(entrada, saida)
cami = acha_caminho(grafo, entrada, saida, chave_inicio)
sequencia = remonta(composicao['d'],composicao['k'],cami, rotulo)

arq = open('resposta.fasta', 'a')
sequencia = '>k={}d={}\n'.format(composicao['k'],composicao['d']) + sequencia + '\n'
arq.write(sequencia)
arq.close()
print("arquivo resposta.fasta gerado com a sequencia.")
