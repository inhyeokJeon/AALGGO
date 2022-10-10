import sys

N = int(sys.stdin.readline().strip())

stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline().strip()))
stairs.append(0)
# stairs.reverse()
# stairs.append(0)

dp = [0] * (N + 2)
dp[1] = stairs[1]
dp[2] = stairs[2] + stairs[1]
for i in range(3, N + 1):
    dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i]

print(dp[N])