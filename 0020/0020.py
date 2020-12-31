import math


def numsum(n):
    if n < 10:
        return n
    else:
        return numsum(n // 10) + n % 10


ans = math.factorial(100)
print(numsum(ans))