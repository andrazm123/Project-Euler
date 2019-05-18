# Z indukcijo dokazemo formuli:
# 1 + 2 + 3 + ... + n = (n * (n + 1)) / 2
# 1 ** 2 + 2 ** 2 + 3 ** 2 + ... + n ** 2 = (n * (n + 1) * (2 * n + 1)) / 6

def razlika_kvadrata_vsote_in_vsote_kvadratov(n):
    '''Izracuna razlko kvadrata vsote in vsote kvadratov prvih n stevil'''
    return int(((n * (n + 1)) / 2) ** 2 - (n * (n + 1) * (2 * n + 1)) / 6)

razlika_kvadrata_vsote_in_vsote_kvadratov(100)