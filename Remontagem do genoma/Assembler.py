import sys
import time

# Abrindo arquivo kdmer
def abrirArquivo():
    try:
        caminho = sys.argv[1]
    except:
        print("Passe o arquivo como arguemento na chamada do programa!" )
        input()
        exit()
    try:
        f = open(caminho, 'r')
    except:
        print("Arquivo não encontrado!!")
        input()
        exit()
    k, d= caminho.split("d")
    k = int(k.split('k')[1])
    d = int(d.split("mer")[0])
    x = f.read()
    x = x.replace("[1]: compositionKD (1000,200) = ", "")
    ls = x.replace('[', "").replace(']', "").replace('\'', "").replace(" ", "").replace("\n","").replace("\r", "").split(',')
    return {'k':k,'d':d,'sequencia':ls}

def su_pre_fixo(i):
    x1 , x2 = i.split('|')
    s1 = x1[1:]
    s2 = x2[1:]
    suf = (s1, s2)
    p1 = x1[0:-1]
    p2 = x2[0:-1]
    pre = (p1, p2)
    return [pre, suf]

def geraAdjLista(composicao):
    grafo = {}
    saida = {}
    entrada = {}
    for x in composicao['sequencia']:
        pre , suf = su_pre_fixo(x)
        grafo[pre] = []
        saida[pre] = 0
        saida[suf] = 0
        entrada[suf] = 0
        entrada[pre] = 0
    for x in composicao['sequencia']:
        pre , suf = su_pre_fixo(x)
        grafo[pre].append(suf)
        saida[pre] += 1
        entrada[suf] += 1
    return [grafo,saida,entrada]

def encontraInicio(entrada, saida):
    mim = 99
    chave = list(entrada)[0]
    lista = []
    for i in list(saida):
        if(entrada[i] == 0):
            lista.append(i)
        if entrada[i] - saida[i] < mim:
            mim = entrada[i] - saida[i]
            chave = i
    return [chave, lista]

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

def remonta(d, k, caminho):
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
    return sequencia + caminho[-2][1][0] + caminho[-1][1]

t1 = time.time()
composicao = abrirArquivo()
print("abrir: ok - ", time.time() - t1,"---" , time.ctime())
t1 = time.time()
grafo, saida, entrada = geraAdjLista(composicao)
d= composicao['d']
k = composicao['k']
print("montar grafo: ok - ", time.time() - t1,"---" , time.ctime())
chave_inicio, lista = encontraInicio(entrada, saida)
t1 = time.time()
cami = acha_caminho(grafo, entrada, saida, chave_inicio)
del grafo
del entrada
del saida
print("caminho euleriano: ok - ", time.time() - t1,"---" , time.ctime())
sequencia = remonta(d,k,cami)
arq = open('resposta.fasta', 'w')
sequencia = '>k={}d={}\n'.format(k,d) + sequencia + '\n'
arq.write(sequencia.__str__())
arq.close()
print("arquivo resposta.fasta gerado com a sequencia.")
input()