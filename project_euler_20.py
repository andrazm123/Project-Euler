def fakulteta(n):
    if n == 0:
        return 1
    else:
        return n * fakulteta(n - 1)

def vsota_stevk_fakultete(n):
    seznam = [int(d) for d in str(fakulteta(n))]  
    vsota = 0
    for i in range(0, len(seznam)):
            vsota = vsota + seznam[i]
    return(vsota)

print(vsota_stevk_fakultete(100))