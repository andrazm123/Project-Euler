def soda_transformacija(stevilo):
    return stevilo / 2

def liha_transformacija(stevilo):
    return 3 * stevilo + 1

def velikost_verige(n):
    stevec = 1
    while n > 1:
        if n % 2 == 0:
            n = soda_transformacija(n)
            stevec = stevec + 1
        else:
            n = liha_transformacija(n)
            stevec = stevec + 1
    return stevec

def najvecja_veriga(meja):
    seznam = []
    i = 1
    while i < meja:
        seznam.append(velikost_verige(i))
        i = i + 1
    return seznam.index(max(seznam)) + 1


print(najvecja_veriga(1000000))