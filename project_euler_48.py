import sys
sys.setrecursionlimit(1500)

def vsota_potenc(n):
    if n == 1:
        return 1
    else:
        return n ** n + vsota_potenc(n - 1)

print(vsota_potenc(1000) % (10 ** 10))