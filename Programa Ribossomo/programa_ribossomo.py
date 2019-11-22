geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L',
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST',
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}



RNAm = input("RNAm: ")

trincas = []
try:
    for i in range(0,len(RNAm),3):
        trincas.append(RNAm[i]+RNAm[i+1]+RNAm[i+2])
except:
    pass    #se não for múltiplo de 3 a ultima a ser descartada

aminoacidos = ""
start = 0
for trinca in trincas:
    try:
        geneticCode[trinca]
    except:
        print("Sequencia errada")
        input()
    if geneticCode[trinca] == "ST":
        break
    if trinca == "AUG":
        start = 1
    if start == 1:
        aminoacidos += geneticCode[trinca]
print("Aminoácidos: "+ aminoacidos)
x = input("ENTER...")
