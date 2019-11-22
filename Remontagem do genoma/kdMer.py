import sys

# Abrindo arquivo .fasta
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
    index = -1
    lista = []
    for linha in f.readlines():
        info = {}
        if linha[0]=='>':
            # Setando 'k' e 'd'
            aux, k, d = linha.split("=")
            k, aux = k.split("d")
            info["k"] = int(k)
            info["d"] = int(d)
            info['sequencia'] = ""
            lista.append(info)
            index += 1
        else:
            lista[index]['sequencia'] += linha.replace("\n", "")
    return lista

# Montando sequencias kdmers
sequencias = abrirArquivo()
for s in sequencias:
    k = s['k']
    d = s['d']
    sequencia = s['sequencia']
    kdmers = []
    for i in range(len(sequencia)-d-k-k+1):
        kdmers.append(sequencia[i:k+i] + "|" + sequencia[i+k+d: k+d+k+i])
    kdmers = sorted(kdmers, key=lambda x:x[0:k])
    arq = open('k{}d{}mer.txt'.format(k, d), 'w')
    arq.write('[')
    a = False
    for i in kdmers:
        if a:
            arq.write(', ')
        a =True
        arq.write('\''+i.__str__()+'\'')
    arq.write(']')
    arq.close()
    print("arquivo k{}d{}mer.txt gerado com as sequencia.".format(k, d))

