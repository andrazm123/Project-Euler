# Znano je, da so Pitagorejske trojice za enačbo a ** 2 + b ** 2 = c ** 2 oblike (Evklidova formula):
# a = m ** 2 - n ** 2
# b = 2 * m * n
# c = m ** 2 + n ** 2
# Velja m > n
# Torej velja a + b + c = 2 * m ** 2 + 2 * m * n = 2 * m * (m + n)
# V naravnih stevilih resujemo enacbo: m * (m + n) = 500

def resitve_enacbe(stevilo):
    '''Vrne celostevilske resitve enacbe m * (m + n) = stevilo'''
    for i in range(1, stevilo + 1):
        for j in range(1, i):
            if i * (i + j) == 500:
                return [i, j]

def zmnozek(vsota):
    '''Vrne zmnozek a * b * c, ce je njihova vsota enaka "vsota"'''
    m = resitve_enacbe(int(vsota / 2))[0] #definirana je le ta sode "vsote"
    n = resitve_enacbe(int(vsota / 2))[1]
    a = m ** 2 - n ** 2
    b = 2 * m * n
    c = m ** 2 + n ** 2
    return a * b * c

zmnozek(500)