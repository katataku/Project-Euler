import math


def numsum(n):
    if n < 10:
        return n
    else:
        return numsum(n // 10) + n % 10


ans = 2 ** 1000
print(numsum(ans))
