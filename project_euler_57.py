# Ulomek bomo pisali kot urejeni par
import math 

stevec = 0
(a, b) = (3, 2)
for i in range(1, 1000):
    (a, b) = ((2 * b + a) // math.gcd(a, b), (a + b) // math.gcd(a, b))
    if len(str(a)) > len(str(b)):
        stevec += 1


print(stevec)