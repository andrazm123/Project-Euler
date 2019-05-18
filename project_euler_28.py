# Poskusimo matematicno poenosaviti problem. Oznacimo z d1, d2, d3 in d4 
# po vrsti diagonale od 1 desno-dol, levo-dol, levo-gor in desno-gor.
# Opazimo, da se vrednosti med vrsticami in stopci med sosednjima 
# diagonalama razlikujeta za 2 * n, (razen med d1 in d4, ki od zdaj naprej nista vec sosednji).
# To je logicno, induktivno dokazimo: za n = 1 prebermo iz diagrama.
# V I.K. pa vidimo, da je vrstica za 2 daljasa od prejsnje (med diagonalama),
# torej je razlika vecja za I.P. + 2. Enako velja za stolpce.
# Opazujmo sedaj le spodnjo desno diagonalo:
# Z malo razmisljanja ugotovimo, da lahko razliko zaporedja stevil v d1 podamo s funkcijo:
# d1(n) = 8 * k - 6, kjer je k k-to zaporedno stevilo v d1.
# Sedaj lahko nalogo enostavno resimo.
# Ker nivoji ustrezajo lihim stevilom bo v diagonali d1 v n-tem nivoju (n + 1) / 2 stevil

def vsota_diagonal(n):
    stevila_v_d1 = [1]
    for i in range(int((n + 1) / 2) - 1):
        stevila_v_d1.append(stevila_v_d1[-1] + 8 * (i + 1) - 6)
    
    vsota_d1 = 0
    for i in range(len(stevila_v_d1)):
        vsota_d1 = vsota_d1 + stevila_v_d1[i]
        
    vsota_d2 = 0
    for i in range(len(stevila_v_d1)):
        vsota_d2 = vsota_d2 + stevila_v_d1[i] + (2 * i)
        
    vsota_d3 = 0
    for i in range(len(stevila_v_d1)):
        vsota_d3 = vsota_d3 + stevila_v_d1[i] + (4 * i)
        
    vsota_d4 = 0
    for i in range(len(stevila_v_d1)):
        vsota_d4 = vsota_d4 + stevila_v_d1[i] + (6 * i)
      
    return vsota_d1 + vsota_d2 + vsota_d3 + vsota_d4 - 3


print(vsota_diagonal(1001))