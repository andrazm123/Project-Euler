def deljenje(n):
    a = 1
    ostanki = []
    while True:
        if a == 0:
            break
        elif 10 * a >= n:
            if (10 * a) % n in ostanki:
                break
            else:
                ostanki.append((10 * a) % n)
            a = (10 * a) % n
        elif (100 * a) >= n:
            ostanki.append(-1)
            if (100 * a) % n in ostanki:
                break
            else:
                ostanki.append((100 * a) % n)
            a = (100 * a) % n
        else:
            ostanki.extend([-1, -1])
            if (1000 * a) % n in ostanki:
                break
            else:
                ostanki.append((1000 * a) % n)
            a = (1000 * a) % n
    if a == 0:
        return 0
    else:
        meja = ostanki.count(a)
        return len(ostanki[meja:]) + 1

st, mx = 2, 1
for i in range(2, 1000):
    if deljenje(i) > mx:
        mx = deljenje(i)
        st = i

print(st)
        