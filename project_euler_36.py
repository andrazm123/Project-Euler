def pretvorba_v_dvojiski(n):
    stevilo = n % 2
    i = 1
    while n > 0:
        n = n // 2
        stevilo = stevilo + (n % 2) * (10 ** i)
        i = i + 1
    return stevilo
 
def ali_je_palindrom(niz):
    '''Preveri ali je stevilo palindrom'''
    dolzina = len(niz)
    if dolzina == 1 or dolzina == 0:
        return True
    elif niz[0] == niz[-1] and ali_je_palindrom(niz[1:-1]) == True:
        return True
    elif niz[0] == niz[-1] and ali_je_palindrom(niz[1:-1]) == False:
        return False
    else:
        return False

def vsota_polindromov_do(n):
    vsota = 0
    for i in range(n):
        if ali_je_palindrom(str(i)) and ali_je_palindrom(str(pretvorba_v_dvojiski(i))):
            vsota = vsota + i
    return vsota

print(vsota_polindromov_do(10 ** 6))