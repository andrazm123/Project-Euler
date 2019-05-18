def stevilo_dni_v_februarju(leto):
    if leto % 400 == 0:
        return 29
    elif leto % 100 == 0:
        return 28
    elif leto % 4 == 0:
        return 29
    else:
        return 28

def st_nedelj(spodnja_meja, zgornja_meja):
    stevec = 1 #leta 1900 je bila nedela 7.1, torej na prvi dan, 7 pa deli 31 + 4
    stevec = (((stevilo_dni_v_februarju(1900) + 365 - 28) % 7) + stevec) % 7 #stevec za 1901, stevec = 2
    i = spodnja_meja
    vsota = 0
    
    while i <= zgornja_meja:
        jan = stevec
        feb = jan + 31
        mar = feb + stevilo_dni_v_februarju(i)
        apr = mar + 31
        maj = apr + 30
        jun = maj + 31
        jul = jun + 30
        avg = jul + 31
        sep = avg + 31
        okt = sep + 30
        nov = okt + 31
        dec = nov + 30
        seznam = [jan, feb, mar, apr, maj, jun, jul, avg, sep, okt, nov, dec]
        j = 0
        while j < 12:
            if seznam[j] % 7 == 0:
                vsota = vsota + 1 
            j = j + 1
        stevec = (dec + 31) % 7
        i = i + 1
    return vsota

st_nedelj(1901,2000)