import sys
from copy import deepcopy
def solve():
    n = int(sys.stdin.readline())
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    dp = deepcopy(num_list)
    now_max = max(dp)
    for i in range(1, n):
        dp[i] = dp[i] + dp[i - 1]
        if dp[i] < 0:
            dp[i] = 0
        else:
            now_max = max(now_max, dp[i])
    return now_max

print(solve())
