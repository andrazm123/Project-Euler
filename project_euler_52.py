def ali_sta_seznama_enaka(sez1, sez2):
    slo1 = {}
    slo2 = {}
    for i in sez1:
        slo1[i] = slo1.get(i, 0) + 1
    for i in sez2:
        slo2[i] = slo2.get(i, 0) + 1
    if slo1 == slo2:
        return True
    else:
        return False

def permutacijsko_stevilo():
    x = 1
    while True:
        sez1 = [int(t) for t in str(x)]
        sez2 = [int(t) for t in str(2 * x)]
        sez3 = [int(t) for t in str(3 * x)]
        sez4 = [int(t) for t in str(4 * x)]
        sez5 = [int(t) for t in str(5 * x)]
        sez6 = [int(t) for t in str(6 * x)]
    
        if ali_sta_seznama_enaka(sez1, sez2) and ali_sta_seznama_enaka(sez1, sez3) and ali_sta_seznama_enaka(sez1, sez4) and ali_sta_seznama_enaka(sez1, sez5) and ali_sta_seznama_enaka(sez1, sez6):
            return x
        x += 1

print(permutacijsko_stevilo())