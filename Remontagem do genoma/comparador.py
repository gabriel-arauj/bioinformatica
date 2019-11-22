import sys

# Abrindo arquivo .fasta
def abrirArquivo(i):
    try:
        caminho = sys.argv[i]
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

arq1 = abrirArquivo(1)
arq2 = abrirArquivo(2)
arq1 = arq1[0]['sequencia']
arq2 = arq2[0]['sequencia']

tam = len(arq1)
""" for i in range(tam):
    print(arq1[i],arq2[i], arq1[i]==arq2[i], ) """
print(tam)
print(arq1 == arq2)