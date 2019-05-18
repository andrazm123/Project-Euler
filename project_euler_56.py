sez = []
for a in range(1, 100):
    for b in range(1, 100):
        vsota = sum([int(k) for k in str(a ** b)])
        sez.append(vsota)

print(max(sez))

