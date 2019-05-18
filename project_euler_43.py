import itertools

seznam = (list(itertools.permutations(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])))


def prastevilsko_stevilo(niz):
    if int(niz[1: 4]) % 2 == 0 and int(niz[2: 5]) % 3 == 0 and int(niz[3: 6]) % 5 == 0 and int(niz[4: 7]) % 7 == 0 and int(niz[5: 8]) % 11 == 0 and int(niz[6: 9]) % 13 == 0 and int(niz[7: 10]) % 17 == 0:
        return True



vsota = 0
for i in seznam:
    if not(int("".join(i)[0]) == 0) and prastevilsko_stevilo(str("".join(i))):
        vsota = vsota + int("".join(i))

print(vsota)