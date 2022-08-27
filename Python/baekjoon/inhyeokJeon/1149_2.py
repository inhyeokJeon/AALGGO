import sys

n = int(sys.stdin.readline().strip())

houses = []

for i in range(n):
    r, g, b = map(int,sys.stdin.readline().strip().split())
    houses.append([r,g,b])

dp = [[0 for _ in range(n) ] for _ in range(3)]

# 빨
dp[0][0] = houses[0][0]
# 초
dp[1][0] = houses[0][1]
# 파
dp[2][0] = houses[0][2]
for i in range(1, n):
    # 해당 인덱스에 i번째는 0 -> 빨, 1 -> 초, 2 -> 파
    dp[0][i] = houses[i][0] + min(dp[1][i-1], dp[2][i-1])
    dp[1][i] = houses[i][1] + min(dp[0][i-1], dp[2][i-1])
    dp[2][i] = houses[i][2] + min(dp[0][i-1], dp[1][i-1])

print(min(dp[0][-1], dp[1][-1], dp[2][-1]))