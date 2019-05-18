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
    if a <= 0: #da lahko izlocimo moznosti v ff(a)
        return -1
    elif a == 1:
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

# Ker vrednosti vedno nastopajo v parih so enolicno dolocene same s sabo f(f(a)) = a



def vsota_do(n):
    kandidati = prastevila_do(n)
    vsota = 0
    j = 1
    while j < n:
        sum_j = vsota_deliteljev(j, kandidati)
        if (not j == sum_j) and sum_j < n and j == vsota_deliteljev(sum_j, kandidati):
            vsota = vsota + (j + sum_j) // 2
        j = j + 1
    return vsota

print(vsota_do(10000))


# Program se ne izracuna v terminalu, iz neznanega razloga,
# a odlicno deluje v core runnerju.

