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

# Ker sta a in b omejena s 1000, nam teorija števil pove,
# da bo vseh prastevil zagotovo manj kot a * b = 10 ** 6

prastevila_01 = prastevila_do(40 ** 2 + 1000 * 40 + 1000)
prastevila = prastevila_do(10 ** 6)

def preveri_formulo(a, b):
    # Prastevila so vecja od 0
    for n in range(40):
        if n ** 2 + a * n + b <= 0:
            return [[a, b], 1]
    
    # Vemo, da obstaja kombinacija za 40 zap. prastevil.
    if 40 ** 2 + a * 40 + b in prastevila_01:
        n = 0
        while n < 10 ** 6:
            if not n ** 2 + a * n + b in prastevila:
                return [[a, b], n]
            n = n + 1
    else:
        return [[a, b], 1]

kandidati = []
prastevila_kandidati = []

# Preprosta teorija stevil pokaze, da ce hocemo, da je zaporednih prastevil
# vec kot 1 morata biti a in b liha.

a = -999
while a < 1000:
    b = -999
    while b <= 1000:
        resitev = preveri_formulo(a, b)
        kandidati.append(resitev[0])
        prastevila_kandidati.append(resitev[1])
        b = b + 2
    a = a + 2

indeks = prastevila_kandidati.index(max(prastevila_kandidati))
rezultat = kandidati[indeks][0] * kandidati[indeks][1]
print(rezultat)

# Program porabi 3 min, kar je zadovoljivo.