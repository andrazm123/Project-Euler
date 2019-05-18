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

def vsota_prastevil(n):
    '''Sesteje prastevila do vklucno n'''
    sez = prastevila_do(n)
    vsota = 0
    for element in sez:
        vsota = element + vsota
    return vsota

print(vsota_prastevil(1999999))
