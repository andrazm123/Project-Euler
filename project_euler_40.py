niz = ""
for i in range(1,1000000):
    niz = niz + str(i)
seznam = [int(d) for d in niz]

print(seznam[0] * seznam[9] * seznam[99] * seznam[999] * seznam[9999] * seznam[99999] * seznam[999999])