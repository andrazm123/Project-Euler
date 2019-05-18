# Omejimo n: 10 ** (n - 1) <= x ** n < 10 ** n
# Torej dobimo 10 ** ((n - 1) / n) <= x < 10
# Vemo, da je x naravno stevilo torej ko bo 10 ** ((n - 1) / n) vecji od 9, usteznih x-ov ne bo vec
# Poracunamo, da so ustrezni n manjsi ali enaki 21

stevilo = 1 
for n in range(1, 22):
    stevilo += 9 - int(10 ** ((n - 1) / n))     
print(stevilo)

# Velja 10 ** ((n - 1) / n) ni naravno stevilo za n > 1
# Za n = 1 smo dodali stevilo = 1