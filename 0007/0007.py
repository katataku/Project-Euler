TARGET = 10001


def getNextPrime(n):
    tar = n + 1
    while True:
        if all(map(lambda x: tar % x != 0, primeList)):
            primeList.append(tar)
            return tar
        else:
            tar += 1


tar = 2
primeList = [2]
for i in range(TARGET - 1):
    tar = getNextPrime(tar)

print(tar)
