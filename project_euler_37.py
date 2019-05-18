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


kandidati = prastevila_do(5000000)


def posebna_prastevila(n):
    vrednost = True
    niz = str(n)
    n2 = n
    t = len(niz)
    for i in niz:
        if n in kandidati:
            n = n // 10
        else:
            vrednost = False
            break
    
    for i in niz:
        if n2 in kandidati and vrednost == True:
            n2 = n2 % (10 ** (t - 1))
            t = t - 1
        else:
            vrednost = False
            break

    return vrednost
    
 

def vsota_posebnih_prastevil(stevilo):
    stevec = 0
    vsota = 0
    for prime in kandidati:
        if posebna_prastevila(prime):
            stevec = stevec + 1
            vsota = prime + vsota
            if stevec == stevilo + 4: #Ker nam računa še 2, 3, 5 in 7.
                return vsota - 2 - 3 - 5 - 7 


print(vsota_posebnih_prastevil(11))
# Računalnik je računal 10 min.











