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

prastevila = prastevila_do(1000000)

vsota = 0
meja = 0
while vsota <= prastevila[-1]:
    vsota += prastevila[meja]
    meja += 1


test = False
for i in range(meja, 0, -1):
    for j in range(0, len(prastevila) - i):
        vsota = sum(prastevila[j: j + i])
        if vsota > prastevila[-1]:
            break
        elif vsota in prastevila[j + i:]:
            test = True
            break
    if test:
        break

print(vsota)