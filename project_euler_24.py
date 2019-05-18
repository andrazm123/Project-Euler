import itertools

def permutacija(n):
    seznam = (list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])))
    vsota = 0
    for i in range(9):
        vsota = (10 ** (9 - i)) * list(seznam[n - 1])[i] + vsota
    return vsota

print(permutacija(1000000))