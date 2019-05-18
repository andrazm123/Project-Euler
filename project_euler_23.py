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

def prastevilski_razcep_stevil(a, kandidati):
    razcep = []
    if a == 1:
        return [[1,1]]
    else:
        for i in kandidati:
            k = 0
            while a % i == 0:
                k = k + 1
                a = a // i
            if not k == 0:
                razcep.append([i,k])
        return razcep


#Vsoto deliteljev izracunamo po znani sigma funkciji.
def vsota_deliteljev(a, kandidati):
    if a == 1:
        return 0
    else:
        sez = prastevilski_razcep_stevil(a, kandidati)
        meja = len(sez)
        i = 0
        vsota = 1
    
        while i < meja:
            vsota = vsota * (sez[i][0] ** (sez[i][1] + 1) - 1) / (sez[i][0] - 1)
            i = i + 1
        return int(vsota) - a

def seznam_posebnih_stevil_do(n):
    seznam = []
    kandidati = prastevila_do(n)
    i = 1
    while i <= n:
        if vsota_deliteljev(i, kandidati) > i:
            seznam.append(i)
        i = i + 1
    return seznam

#print(seznam_posebnih_stevil_do(29000))

def stevila_ki_se_jih_ne_da_zapisati(n):
    moznosti = [True for i in range(n)]
    sez = seznam_posebnih_stevil_do(n)
    i = 0
    while i < len(sez):
        j = 0
        while j <= i:
            t = sez[i] + sez[j]
            if t <= n:
                moznosti[t - 1] = False
            j = j + 1
        i = i + 1
    
    vsota = 0
    r = 0
    while r < n:
        if moznosti[r] == True:
            vsota = vsota + (r + 1)
        r = r + 1
    return vsota

print(stevila_ki_se_jih_ne_da_zapisati(30000))





    



