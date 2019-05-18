# Dokazimo, da so iskana stevila najvec 5-mestno. Naj bo A n-mestno stevilo.
# Vsota petih potenc njegovih stevk: B = n * (9 ** 5)
# Stevilo samo pa je najvec:
# A = 9 * (10 ** (n - 1) + 10 ** (n - 2) + ... + 1) = 9 * (10 ** n  / (10 - 1)) = 
#   = 10 ** n - 1
# Dokazimo, da za n > 5 velja B < A, n * (9 ** 5) < 10 ** n - 1, 
# to dokazemo tako: velja za n = 6, z odvodi, pa vidimo, da desna stran hitreje narasca kot leva.
# Torej so iskana stevila najvec 5 mestna.

seznam = list(range(2, 1000000)) #Saj stevilo 1 ne steje
resitve = []

for i in seznam:
    stevke = [int(d) for d in str(i)]
    vsota = 0
    for j in range(len(stevke)):
        vsota = vsota + stevke[j] ** 5
    if i == vsota:
        resitve.append(i)

koncna_vsota = 0
for k in range(len(resitve)):
    koncna_vsota = koncna_vsota + resitve[k]

print(koncna_vsota) 
