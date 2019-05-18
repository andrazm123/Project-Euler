# Ker je stevilo manjse od 100 lahko poisceno tabelo prvih 100 prastevil.
prastevila = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def razcep(stevilo):
    razcep = {}    
    for i in prastevila:
        while stevilo % i == 0:
            razcep[i] = razcep.get(i, 0) + 1
            stevilo = stevilo // i
    return razcep
        
def faktorizacija_ulomka(stevec, imenovalec):
    raz_ime = razcep(imenovalec)
    raz_ste = razcep(stevec)
    for i in raz_ime.keys():
        if not raz_ste.get(i, 0) == 0:
            if raz_ime[i] >= raz_ste[i]:
                stevec = stevec // (i ** raz_ste[i])
                imenovalec = imenovalec // (i ** raz_ste[i])
            else:
                stevec = stevec // (i ** raz_ime[i])
                imenovalec = imenovalec // (i ** raz_ime[i])
    return (stevec, imenovalec)


zmnozek_ime = 1
zmnozek_ste = 1
for ime in range(11, 100):
    for ste in range(11, ime):
        for test in range(1, 10):
            if str(test) in str(ste) and str(test) in str(ime):
                ste1 = int(str(ste).replace(str(test), "", 1))
                ime1 = int(str(ime).replace(str(test), "", 1))
                if ste1 * ime == ste * ime1:
                    (a, b) = faktorizacija_ulomka(ste, ime)
                    zmnozek_ime *= b
                    zmnozek_ste *= a

(st, im) = faktorizacija_ulomka(zmnozek_ste, zmnozek_ime)
print(im)


