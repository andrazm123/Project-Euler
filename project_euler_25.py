def fibonacci(n):
    seznam = []
    (a, b) = (0, 1)
    for i in range(n):
        (a, b) = (b, a+b)
        seznam.append(a)
    return [a, seznam]

def stevke(stevilo):
    n = 1
    while n > 0: #nevem kako naj bolje napisem
        if fibonacci(n)[0] > 10 ** (stevilo -1):
            return fibonacci(n)[1].index(fibonacci(n)[0]) + 1
        n = n + 1

print(stevke(1000))