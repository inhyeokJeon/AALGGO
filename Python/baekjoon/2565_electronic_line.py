import sys


def solve():
    N = int(sys.stdin.readline().strip())
    lines = []
    dp = [1] * N
    # LIS 알고리즘으로 해결해야함.
    for _ in range(N):
        lines.append(list(map(int, sys.stdin.readline().strip().split())))
    lines.sort()

    for i in range(1, len(lines)):
        for j in range(i):
            if lines[i][1] > lines[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return N - max(dp)

print(solve())




