def vsota_stevk_potence_2(n):
    seznam = [int(d) for d in str(2 ** n)]  
    vsota = 0
    for i in range(0, len(seznam)):
            vsota = vsota + seznam[i]
    return(vsota)

print(vsota_stevk_potence_2(1000))