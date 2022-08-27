import sys

def solve():
    n = int(sys.stdin.readline().strip())

    sequence = list(map(int,sys.stdin.readline().strip().split()))
    if n == 1:
        return 1
    dp = [1] * n
    dp2 = [1] * n
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    for i in range(n-2, -1, -1):
        for j in range(i + 1, n):
            if sequence[i] > sequence[j]:
                dp2[i] = max(dp2[i], dp2[j] + 1)

    ret = 0
    for i in range(n):
        ret = max(ret, dp[i] + dp2[i] - 1)

    return ret

print(solve())
