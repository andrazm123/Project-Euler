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

def seznam_tromestnih_zmozkov(zacetek, konec):
    '''Vrne seznam zmozkov stevil od zacetek do konec'''
    seznam = []
    for i in range(zacetek, konec + 1):
        for j in range(zacetek, i + 1):
            seznam.append(i * j)
    return seznam

def poisci_palindrom(zacetek, konec):
    '''Poisce najvecji palindrom med zmnozki od zacetek do konec'''
    seznam = seznam_tromestnih_zmozkov(zacetek, konec)
    while len(seznam) > 0:
        kandidat = [int(d) for d in str(max(seznam))]
        if ali_je_palindrom(kandidat):
            break
        seznam.remove(max(seznam))
    return max(seznam)
    
poisci_palindrom(100,999)

        

