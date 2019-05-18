def prastevila_do(n):
    kandidati = [False]
    prastevila = []
    i = 2
    j = 2
 
    while i <= n:
        kandidati.append(True)
        i = i + 1
    
    while j <= int(round(n ** (1 / 2) + 1, 0)):    
        k = 2
        while j * k <= n:
            kandidati[j * k - 1] = False
            k = k + 1
        j = j + 1
    
    r = 0
    while r < n:
        if kandidati[r] == True:
            prastevila.append(r + 1)
        r = r + 1
    return prastevila

kandidati = prastevila_do(1000000)

def vec_kot_4_delitelji(stevilo):
    stevec = 0
    for i in range(len(kandidati)):
        if stevilo % kandidati[i] == 0:
            stevec = stevec + 1
        if stevec == 4:
            return True
    if stevec < 4:
        return False

# Funkcija bi lahko sprejela argument meja, do kam bi računala, a bi potem moral komplicirati,
# če bi želel praštevilse kandidate izračunati le enkrat, ker funkcija išče le najmanjšo število
# z neko lastnostjo, je lažje, da mejo ročno popravim (drugače bi bilo, če bi lahko funkcijo uporabili
# tudi za kakšne druge stvari, ki bi bile dejansko odvisne od meje).

def stiri_zaporedna_stevila_do():
    for i in range(10000, 1000000):
        if vec_kot_4_delitelji(i) and vec_kot_4_delitelji(i + 1) and vec_kot_4_delitelji(i + 2) and vec_kot_4_delitelji(i + 3):
            return i
    return False


print(stiri_zaporedna_stevila_do())

# Program je računal 1h ...