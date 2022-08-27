import sys

def solve():
    n = int(sys.stdin.readline().strip())

    sequence = list(map(int,sys.stdin.readline().strip().split()))
    if n == 1:
        return 1
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(solve())
