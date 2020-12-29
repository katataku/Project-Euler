TAR = 1000000


def Collatz(n):
    nextTerm = n // 2 if n % 2 == 0 else (n * 3) + 1
    if n < TAR:
        if memo[n] == -1:
            memo[n] = Collatz(nextTerm) + 1
        return memo[n]
    else:
        return Collatz(nextTerm) + 1


memo = [-1 for i in range(TAR)]
memo[1] = 1


ans = 0
for i in range(1, TAR):
    ans = max(ans, Collatz(i))

print(memo.index(ans))