import sys

N, K = list(map(int,sys.stdin.readline().strip().split()))
bags = []
dp = [[0] * (K + 1) for _ in range(N+1)] # 무게, 가치
for _ in range(N):
    bags.append(list(map(int,sys.stdin.readline().strip().split())))

for i in range(1, N+1): # 물건 index
    for j in range(1, K+1): # 무게
        weight = bags[i - 1][0]
        value = bags[i - 1][1]
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[N][K])