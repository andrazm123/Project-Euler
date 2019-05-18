def stevilo_potenc(meja):
    seznam = []
    a = 2
    while a <= meja:
        b = 2
        while b <= meja:
            moznost = a ** b
            if not moznost in seznam:
                seznam.append(moznost)
            b = b + 1
        a = a + 1
    return len(seznam)

print(stevilo_potenc(100))