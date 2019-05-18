# Varno je reči, da so vse besede dolžin manjsših od 30 znakov.
# Angleška abeceda ima 26 črk, torej bo majvečja vrednost
# besede manjša od 30 * 26.

abeceda = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def trikotniska_stevila_do(meja):
    trikotniska_stevila = []
    for n in range(1, meja):
        stevilo = int((1 / 2) * n * (n + 1))
        if stevilo <= meja:
            trikotniska_stevila.append(stevilo)
        else:
            break
    return trikotniska_stevila

# Datoteka se nahaja na Project Euler pod spodnjim imenom.
datoteka = open("podatki\p042_words.txt",'r') # r je branje
besede = sorted(datoteka.read().replace('"','').split(",")) #sorted = abecedni red

def vrednost_besede(niz):
    beseda = list(niz)
    vrednost = 0
    for i in abeceda:
        while i in beseda:
            vrednost = abeceda.index(i) + 1 + vrednost
            beseda.remove(i)
    return vrednost

trikotniska_stevila = trikotniska_stevila_do(30 * 26)
stevec = 0
for element in besede:
    if vrednost_besede(str(element)) in trikotniska_stevila:
        stevec = stevec + 1

print(stevec)
