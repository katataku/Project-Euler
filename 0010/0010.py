import math

TARGET = 2000000
primeList = range(TARGET + 1)[2:]
idx = 0
while primeList[idx] < math.sqrt(TARGET):
    tar = primeList[idx]
    primeList = list(filter(lambda x: (x % tar != 0 or x == tar), primeList))
    idx += 1


print(sum(primeList))
