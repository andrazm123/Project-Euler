def stevilo_deliteljev(n):
    meja = n + 1
    delitelji = []
    if n == 1:
        return 1
    else:
        for i in range(2, meja):
            k = 1
            seznam = []
            while n % i == 0:                
                seznam.append(i ** k)
                k = k + 1
                n = int(n / i)
            i = i + 1
            if len(seznam) > 0:
                delitelji.append(seznam)
        
        #print(delitelji)
        zmnozek = 1
        for i in delitelji:
            zmnozek = zmnozek * (len(i) + 1)
        # Dolzina i je ravno eksponent na prastevilu,
        # znana formula za stevilo deliteljev je ravno (i1 + 1) * ... * (ik + 1)
        return zmnozek

stevilo_deliteljev(12)

# Trikotniska stevila so oblike n * (n + 1) / 2
# BSŠ: Je n sodo stevilo.
# Stevili n / 2 in n + 1 sta si tuji, zato je stevilo njujnih deliteljev
# kar enako stevilo deliteljev od n / 2 pomnozeno s stevilo deliteljev od n + 1.

def trikotnisko_stevilo(n):
    i = 1
    while i >= 1:
        if stevilo_deliteljev(i) * stevilo_deliteljev(int((i + 1) / 2)) > n:
            break
        else:
            i = i + 2
    j = 2
    while j > 1:
        if stevilo_deliteljev(int(j / 2)) * stevilo_deliteljev(i + 1) > n:
            break
        else:
            j = j + 2

    return int(max(i, j) * (max(i, j) + 1) / 2)

print(trikotnisko_stevilo(500))