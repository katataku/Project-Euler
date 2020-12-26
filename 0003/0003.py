TARGET = 600851475143


def getNextPrime(n):
    global prime
    tar = n + 1
    while True:
        if all(map(lambda x: tar % x != 0, primeList)):
            primeList.append(tar)
            return tar
        else:
            tar += 1


prime_max = 1
primeList = [2]
prime = 2
tar = TARGET
while tar != 1:
    if tar % prime == 0:
        tar = tar // prime
        prime_max = prime
    prime = getNextPrime(prime)

print(prime_max)
