def gcd(a, b):
    '''Najvecji skupni veckratnik'''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    '''Najmanjsi skupni delitelj'''
    return int((a * b) / gcd(a, b))

def stevilo_deljivo_prvimi_stevili(n):
    '''Vrne najmanjso stevilo deljivo s prvimi n naravnimi stevili'''
    if n == 1:
        return 1
    else:
        return lcm(n, stevilo_deljivo_prvimi_stevili(n - 1))

print(stevilo_deljivo_prvimi_stevili(20))


