def ali_je_palindrom(niz):
    '''Preveri ali je stevilo palindrom'''
    dolzina = len(niz)
    if dolzina == 1 or dolzina == 0:
        return True
    elif niz[0] == niz[-1] and ali_je_palindrom(niz[1:-1]) == True:
        return True
    elif niz[0] == niz[-1] and ali_je_palindrom(niz[1:-1]) == False:
        return False
    else:
        return False

def seznam_v_stevilo_obratno_stevilo(seznam):
    stevilo = 0
    for i, j in enumerate(seznam):
        stevilo += j * 10 ** i
    return stevilo

rezultat = 0
for i in range(1, 10000):
    stevec = 0
    sez = [int(k) for k in str(i)]
    kandidat = i
    while stevec < 50:
        kandidat = kandidat + seznam_v_stevilo_obratno_stevilo(sez)
        sez = [int(k) for k in str(kandidat)]
        if ali_je_palindrom(sez):
            stevec = 50
            rezultat += 1
        else:
            stevec = stevec + 1

print(9999 - rezultat)
    
