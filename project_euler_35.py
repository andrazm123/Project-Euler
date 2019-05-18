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

kandidati = prastevila_do(10 ** 6)

def ciklicno_prastevilo(n):
    if n in [2, 3, 5, 7]:
        return True
    else:
        stevke = [int(d) for d in str(n)]
        vrednost = True
        stevilo = n
        for i in range(len(stevke)):
            enice = stevilo % 10
            ostalo = stevilo // 10
            stevilo = int(str(enice) + str(ostalo))
            if not (stevilo in kandidati):
                vrednost = False
        return vrednost


stevec = 0
for i in kandidati:
    if ciklicno_prastevilo(i) == True:
        stevec = stevec + 1

print(stevec)


# Progam porabi skoraj 15 min, a deluje, nevem kako bi ga bistevno izboljsal,
# Male optimizacije so seveda se mogoce, kot so zozitev kandidatov in podobno.




