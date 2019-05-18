# Ker je 100 * 100 = 10000 in ima ta izraz 3 + 3 + 6 = 11 stevk
# in 1 * 10000 = 10000 in ima ta izraz 1 + 5 + 5 = 11 stevk,
# je dovolj preveriti le produkte dvomestnega stevila s petmestnim.


seznam = []
for i in range(1, 100):
    i_stevke = [int(d) for d in str(i)]
    for j in range(1, 100000):
        j_stevke = [int(d) for d in str(j)]
        
        vrednost1 = True
        for k in i_stevke:
            if k in j_stevke:
                vrednost1 = False
        if vrednost1 == True:   
            ij_stevke = [int(d) for d in str(i * j)]
            vrednost2 = True
            for ij in ij_stevke:
                if (ij in i_stevke) or (ij in j_stevke):
                    vrednost2 = False
            if vrednost2 == True:
                stevke = i_stevke + j_stevke + ij_stevke
                vrednost4 = True
                for l in range(1, 10):
                    if l in stevke:
                        stevke2 = stevke + [10] # da spremenimo seznam
                        stevke2.remove(l)
                        if l in stevke2 or 0 in stevke:
                            vrednost4 = False
                    else:
                        vrednost4 = False                    
                if vrednost4 == True and not((i * j) in seznam):
                    seznam.append(i * j)

vsota = 0
for stevilo in seznam:
    vsota = vsota + stevilo

print(vsota)

            
            
      

        

