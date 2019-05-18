def najvecji_prastevilski_delitelj(n):
    meja = n + 1
    if n == 1:
        return "neobstaja"
    else:
        for i in range(2, meja):
            while n % i == 0:
                n = int(n / i)
                if n == 1:
                    return i
            i = i + 1

print(najvecji_prastevilski_delitelj(600851475143))