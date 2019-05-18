# Po Evklidovem izreku vemu, da se da vsako pitagorejsko trojico 
# enolično zapisati kot a = k * (m ** 2 - n ** 2),
# b = k * 2 * m * n in c = k * (m ** 2 + n ** 2), kjer velja
# m > n, gcd(m, n) = 1 in eden izmed m in n je deljiv z 2. 
# Če malo premečemo enačbe, se izkaže, da je dovolj preveriti le 
# m-je do 25 in k-je do 250.

from statistics import mode

def gcd(a, b):
    '''Najvecji skupni veckratnik'''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

seznam = []
for m in range (1, 25):
    for n in range (1, m):
        for k in range(1, 125):
            if (m % 2 == 0 or n % 2 == 0) and gcd(m, n) == 1 and 2 * m * (m + n) * k <= 1000:
                seznam.append(2 * m * (m + n) * k)

print(mode(seznam))