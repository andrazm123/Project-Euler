# fi funkcija ima enacbo:
# n/fi(n) = 1 / ((1 - 1 / p1) *** (1 - 1 / pm)) = (p1 * *** * pm) / ((p1 - 1) * *** * (pm - 1))

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

kandidati = prastevila_do(1000)

# ce je n prastevilo je n/fi(n) = p / (p - 1) <= 2, torej vemo da je ze za n = 6 vecje.

def faktorizacija(n):
    sez = []
    for i in kandidati:
        if i <= n and n % i == 0:
            sez.append(i)
            n = n // i
    if sez == []:
        sez.append(0)
    return sez

def izracuna_nfi(n):
    produkt = 1
    for i in faktorizacija(n):
        produkt *= i / (i - 1)
    return produkt

maxi = []
for i in range(1, 1000001):
    maxi.append(izracuna_nfi(i))
    
print(maxi.index(max(maxi)) + 1)










