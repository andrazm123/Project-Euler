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


prastevila = prastevila_do(10000)

for i in prastevila:
    if i > 1000:
        for j in range(1,5000):
            if not(i == 1487) and i + j in prastevila and i + 2 * j in prastevila:
                mnozica_i = set([int(d) for d in str(i)])
                mnozica_ij = set([int(d) for d in str(i + j)])
                mnozica_ijj = set([int(d) for d in str(i + j + j)])
                if mnozica_i == mnozica_ij and mnozica_i == mnozica_ijj:
                    print(str(i) + str(i + j) + str(i + j * 2))

