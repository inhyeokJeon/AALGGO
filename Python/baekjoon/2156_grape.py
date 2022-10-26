import sys

N = int(sys.stdin.readline().strip())
def solve():
    grape = [0]
    dp = [0] * (N + 1)
    for i in range(N):
        grape.append(int(sys.stdin.readline().strip()))
    if N <= 2:
        return sum(grape)
    # if N == 3:
    #     return max(grape[1] + grape[2], grape[0] + grape[2], grape[0] + grape[1])

    dp[1] = grape[1]
    dp[2] = grape[1] + grape[2]
    # dp[3] = max(grape[1] + grape[2], grape[0] + grape[2], grape[0], grape[1])
    for i in range(3, N + 1):
        dp[i] = max(dp[i-2] + grape[i],  dp[i-3] + grape[i-1] + grape[i], dp[i-1])

    return dp[N]
print(solve())




