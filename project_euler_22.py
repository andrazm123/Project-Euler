abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def abecedna_vrednost(ime):
    seznam = list(str(ime))
    vrednost = 0
    for i in range(len(seznam)):
        vrednost = vrednost + abeceda.index(seznam[i]) + 1
    return vrednost

# Datoteka se nahaja na Project Euler pod spodnjim imenom.
datoteka = open("podatki\p022_names.txt",'r') # r je branje
imena = sorted(datoteka.read().replace('"','').split(",")) #sorted = abecedni red

def vsota(seznam):
    vsota = 0
    for i in range(len(seznam)):
        vsota = vsota + (i + 1) * abecedna_vrednost(seznam[i])
    return vsota

print(vsota(imena))