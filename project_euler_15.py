# Stevilo poti lahko izracunamo kombinatoricno.
# Da pridemo iz zgornjega levega v spodni desni kot
# tabele n krat n bomo potrebovali 2n potez.
# Od tega se bomo n krat premaknili navzdol.
# Torej je vseh moznosti toliko, kolikor je moznosti
# da med 2n elementi izberemo n elementov,
# kjer 2n elementov predstavlja poteze,
# n pa tiste poteze na katerih se premaknemo navzdol.
# Torej je vseh moznosti ravno 2n nad n.
# 2n nad n = 2n! / ((n!) ** 2)

def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def stevilo_poti_tabele(n):
    return int(fakulteta(2 * n) / ((fakulteta(n)) ** 2))

print(stevilo_poti_tabele(20))