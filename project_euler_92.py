def nova_stevka(n):
    return sum([int(i) ** 2 for i in str(n)])

bolean = [None for a in range(0, 567)]
bolean[1 - 1] = True
bolean[89 - 1] = False

stevec = 0
for i in range(1, 10000000):
    sez = []
    while True:
        i = nova_stevka(i)
        sez.append(i)
        if bolean[i - 1] == False:
            stevec += 1
            for i in sez:
                bolean[i - 1] = False
            break
        elif bolean[i - 1]:
            for i in sez:
                bolean[i - 1] = True
            break

print(stevec)
