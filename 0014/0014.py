TAR = 1000000


def Collatz(n):
    if n < TAR:
        if memo[n] == -1:
            if n % 2 == 0:
                memo[n] = Collatz(n // 2) + 1
            else:
                memo[n] = Collatz((n * 3) + 1) + 1
        return memo[n]
    else:
        if n % 2 == 0:
            return Collatz(n // 2) + 1
        else:
            return Collatz((n * 3) + 1) + 1


memo = [-1 for i in range(TAR + 10)]
memo[1] = 1


ans = 0
for i in range(1, TAR):
    ans = max(ans, Collatz(i))

print(memo.index(ans))