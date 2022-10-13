import sys

N = int(sys.stdin.readline().strip())

# 처음은 3으로 나눈거 두번짼 2로 나눈거 세번째 1을 뺀거
dp = [0] * (N + 1)


def solve():
    for i in range(1, N + 1):
        temp = []
        if i % 3 == 0:
            temp.append(min(dp[(i // 3)], dp[i - 1]) + 1)
        if i % 2 == 0:
            temp.append(min(dp[(i // 2)], dp[i - 1]) + 1)
        temp.append(dp[i - 1] + 1)
        dp[i] = min(temp)
    return dp[N] - 1
print(solve())