with open('p067_triangle.txt', 'r') as dat:
    seznam = dat.read().strip().split("\n")

#print(seznam)
trikotnik = []
for i in range(len(seznam)):
    x = seznam[i].split()
    y = [int(t) for t in x]
    trikotnik.append(y)


for j in range(len(trikotnik) - 1):
	t = len(trikotnik) - j - 1
	for i in range(len(trikotnik[t]) - 1):
		trikotnik[t - 1][i] += max(trikotnik[t][i], trikotnik[t][i + 1])

print(trikotnik[0][0])

