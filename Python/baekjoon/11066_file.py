import sys
T = int(sys.stdin.readline().strip())

for t in range(T):
    N = int(sys.stdin.readline().strip())
    files = [0] + list(map(int, sys.stdin.readline().strip().split()))
    if len(files) == 3:
        print(sum(files))
        continue

    S = [0] * (N + 1)
    for i in range(1, N + 1):
        S[i] = S[i - 1] + files[i]
    dp = [[0] * (N+1) for i in range(N+1)]

    for i in range(2, N + 1): # 부분 파일의 길이
        for j in range(1, N - i + 2): # 시작점
            dp[j][i + j - 1] = min([dp[j][j + k] + dp[j+ k + 1][j + i - 1] for k in range(i - 1)]) + (S[i + j - 1] - S[j - 1])


    print(dp[1][-1])

"""
1
4
40 30 30 50
"""

"""
2
4
40 30 30 50
15
1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
"""

