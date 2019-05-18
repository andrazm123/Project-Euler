def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(10)

def vsota(meja):
    vsota = 0
    n = 1
    while fibonacci(n) <= meja:
        if fibonacci(n) % 2 == 0:
            vsota = vsota + fibonacci(n)
        else:
            vsota = vsota
        n = n + 1
    return vsota

print(vsota(4000000))