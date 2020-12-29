TAR = 500


def makeDivList(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


s = 0
cnt = 0
cdList = []

while len(cdList) < TAR:
    cnt += 1
    s += cnt
    cdList = makeDivList(s)

print(s)
