# Če obrnemo enačbo za pentagonalno število, dobimo, da je x pentagonalno
# natanko tedaj ko je (1 + 24 * x) ** (1 / 2) + 1 deljivo s 6.
# Podobno dobimo, če obrnemo enačbo za heksagonalno število, x je 
# je ksagonalno število natanko takrat ko velja: (1 + 8 * x) ** (1 / 2) + 1 je delivo s 4.

def tri_pet_heks_stevilo(meja):
    i = meja
    while i > 0:
        trikotnisko = int(i * (i + 1) / 2)
        kandidat_5 = (1 + 24 * trikotnisko) ** (1 / 2)
        kandidat_6 = (1 + 8 * trikotnisko) ** (1 / 2)
        if (kandidat_5).is_integer() and (kandidat_6).is_integer():
            if (int(kandidat_5) + 1) % 6 == 0 and (int(kandidat_6) + 1) % 4 == 0:
                return trikotnisko
        i = i + 1

# Ker vemo, da je T_285 iskano stevilo moramo vzeti vecji stevec
print(tri_pet_heks_stevilo(286))




