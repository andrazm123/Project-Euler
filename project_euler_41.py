# Načeloma bi morali preveriti vsa prastevila do devetmestnih
# a se iskaže, da 3 | 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 in tudi
# 3 | 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8, torej je dovolj preveriti
# le praštevila do 7700000

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


def ali_je_pandigital(niz):
    dolzina = len(niz)
    for i in range(1, dolzina + 1):
        if not(str(i) in niz):
            return False
    return True

def najvecje_posebno_prastevilo(meja):
    kandidati_demo = prastevila_do(meja)
    kandidati = kandidati_demo[::-1]
    for prime in kandidati:
        if ali_je_pandigital(str(prime)):
            return prime

print(najvecje_posebno_prastevilo(7700000))