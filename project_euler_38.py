# Opazimo lahko, da je n <= 5, če bi bil n > 5, bi imeli zmnozki
# vecjo vsoto stevk kot 9, torej ne bi bili pandigital.
# Opazimo lahko tudi, da je stevilo s katerim bomo množili n največ štirimestno

def ali_je_pandigital(niz):
    if len(niz) == 9 and "1" in niz and "2" in niz and "3" in niz and "4" in niz and "5" in niz and "6" in niz and "7" in niz and "8" in niz and "9" in niz:
        return True
    else:
        return False

def najvecji_prdukt():
    kandidati = ["0"]
    for kandidat in range(1, 10):
        niz = str(1 * kandidat) + str(2 * kandidat) + str(3 * kandidat) + str(4 * kandidat) + str(5 * kandidat)
        if ali_je_pandigital(niz):
            kandidati.append(niz)

    for kandidat in range(10, 100):
        niz = str(1 * kandidat) + str(2 * kandidat) + str(3 * kandidat) + str(4 * kandidat)
        if ali_je_pandigital(niz):
            kandidati.append(niz)

    for kandidat in range(100, 1000):
        niz = str(1 * kandidat) + str(2 * kandidat) + str(3 * kandidat)
        if ali_je_pandigital(niz):
            kandidati.append(niz)

    for kandidat in range(1000, 10000):
        niz = str(1 * kandidat) + str(2 * kandidat)
        if ali_je_pandigital(niz):
            kandidati.append(niz)
    
    return max(kandidati)

print(najvecji_prdukt())