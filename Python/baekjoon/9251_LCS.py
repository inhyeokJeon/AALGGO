import sys


def solve():
    l1 = sys.stdin.readline().strip()
    l2 = sys.stdin.readline().strip()
    dp = [[0] * (len(l2) + 1) for _ in range(len(l1) + 1)]
    for i in range(1, len(l1) + 1):
        for j in range(1, len(l2) + 1):
            if l1[i - 1] == l2[j - 1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # for d in dp:
    #     print(d)

    return dp[-1][-1]
print(solve())




