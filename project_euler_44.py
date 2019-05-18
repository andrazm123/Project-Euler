# Če obrnemo enačbo za pentagonalno število, dobimo, da je x pentagonalno
# natanko tedaj ko je (1 + 24 * x) ** (1 / 2) + 1 deljivo s 6.

def test_pentagonalnosti_vsote_in_razlike(n, m): 
    stevilo1 = (1 + 12 * (3 * (n ** 2 + m ** 2) - n - m)) ** (1 / 2)
    stevilo2 = (1 + 12 * (3 * (n ** 2 - m ** 2) - n + m)) ** (1 / 2)
    if (stevilo1).is_integer() and (stevilo2).is_integer():
        if (int(stevilo1) + 1) % 6 == 0 and (int(stevilo2) + 1) % 6 == 0:
            return True
    else:
        return False

def prva_resitev_do(meja):
    kandidati = []
    for n in range(1, meja):
        for m in range(1, n):
            if test_pentagonalnosti_vsote_in_razlike(n, m):
                kandidati.append(int((3 * (n ** 2 - m ** 2) - n + m) / 2))
    
    return min(kandidati)

print(prva_resitev_do(4000000))

# Če vstavimo, majhno mejo, dobimo rešitev 5482660, a ne vemo, če je to res najmanjsa.
# vemo, da so rešitve oblike: (n - m) * (3 * (n + m) - 1) / 2,
# ko n preseže 4000000 torej ni več manjših rešitev.
# Sedaj le še spustimo program za mejo 4000000 in vidimo, da je 5482660 res najmanjsa resitev.

