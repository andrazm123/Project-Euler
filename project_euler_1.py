def vsota_deliteljev_3_5(meja):
    vsota = 0
    for n in range(1, meja):
        if n % 5 == 0 or n % 3 == 0:
            vsota = n + vsota
    return vsota

print(vsota_deliteljev_3_5(1000))

