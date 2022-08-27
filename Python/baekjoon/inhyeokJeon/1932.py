import sys
from copy import deepcopy
n = int(sys.stdin.readline().strip())

triangle = []
dp = []
for i in range(n):
    temp = list(map(int,sys.stdin.readline().strip().split()))
    triangle.append(temp)

dp = deepcopy(triangle)
for i in range(n - 2, -1, -1):
    for j in range(i+1):
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])


print(dp[0][0])