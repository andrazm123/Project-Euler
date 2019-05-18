def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def kombinacije(n, r):
    return int(fakulteta(n) / (fakulteta(r) * fakulteta(n - r)))

def koliko_velikih_kombinacij(meja):
    stevec = 0
    for n in range(1, 101):
        for u in range(1, n + 1):
            if kombinacije(n, u) > meja:
                stevec += 1
    return stevec

print(koliko_velikih_kombinacij(1000000))
