# Preprosta neenakost: 9! * n < 10 ** (n - 1), nam pokaže, 
# da moramo preveriti le vrednosti do za n <= 8, kjer 
# n predstavlja stevilo stevk, torej le števila do 9! * 8 < 3 * 10 ** 6

def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def curious_numbers(n):
    stevke = [int(d) for d in str(n)]
    vsota_fakultet = 0
    for i in stevke:
        vsota_fakultet = vsota_fakultet + fakulteta(i)
    if vsota_fakultet == n:
        return True
    else:
        return False

vsota = 0
for kandidat in range(3, 3 * 10 ** 6): # Saj 1 in 2 ne štejeta
    if curious_numbers(kandidat):
        vsota = vsota + kandidat

print(vsota)
