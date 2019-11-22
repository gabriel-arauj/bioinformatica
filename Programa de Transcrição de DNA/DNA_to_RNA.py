dna = "GGC.CGA.TTA.ATG.CTT.AAA.TGC.GGC.CTA.AAT.TAT"
rna = ""

for nucleotideo in dna:
  if nucleotideo == "G":
    rna += "C"
  if nucleotideo == "C":
    rna += "G"
  if nucleotideo == "A":
    rna += "U"
  if nucleotideo == "T":
    rna += "A"
  if nucleotideo == ".":
    rna += "."
print(dna)
print(rna)