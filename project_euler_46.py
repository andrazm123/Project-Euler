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


def goldbachova_domneva_do(meja):
    primes = prastevila_do(meja)
    for i in range(9, meja, 2):
        vrednost = True
        for j in range(len(primes)):
           stevilo = int((i - primes[j]) / 2)
           if stevilo >= 0 and (stevilo ** (1/2)).is_integer():
               vrednost = False
        if vrednost:
            return i

print(goldbachova_domneva_do(10000))