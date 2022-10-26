import sys
N, M, K = list(map(int,sys.stdin.readline().strip().split()))
chess = [None] * N
black_tables = [[0] * (M + 1) for _ in range(N + 1)]
white_tables = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(N):
    chess[i] = sys.stdin.readline().strip()
# 검정 시작
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == j == 1:
            if chess[i - 1][j - 1] == "B":
                black_tables[i][j] = 0
                white_tables[i][j] = 1
            else:
                black_tables[i][j] = 1
                white_tables[i][j] = 0
        if (i + j) % 2 == 0: # 대각선 부분이 검정 자리일 때 # 흰색 자리일 때
            if chess[i-1][j-1] == "B":
                black_tables[i][j] = black_tables[i-1][j] + black_tables[i][j-1] - black_tables[i-1][j-1]
                white_tables[i][j] = white_tables[i - 1][j] + white_tables[i][j - 1] - white_tables[i - 1][j - 1] + 1
            else:
                black_tables[i][j] = black_tables[i - 1][j] + black_tables[i][j - 1] - black_tables[i - 1][j - 1] + 1
                white_tables[i][j] = white_tables[i - 1][j] + white_tables[i][j - 1] - white_tables[i - 1][j - 1]
        else: # 그 반대일 때
            if chess[i-1][j-1] == "B":
                black_tables[i][j] = black_tables[i-1][j] + black_tables[i][j-1] - black_tables[i-1][j-1] + 1
                white_tables[i][j] = white_tables[i - 1][j] + white_tables[i][j - 1] - white_tables[i - 1][j - 1]
            else:
                black_tables[i][j] = black_tables[i - 1][j] + black_tables[i][j - 1] - black_tables[i - 1][j - 1]
                white_tables[i][j] = white_tables[i - 1][j] + white_tables[i][j - 1] - white_tables[i - 1][j - 1] + 1

result = float("inf")
for i in range(1, N - K + 2):
    for j in range(1, M - K + 2):
        total = K * K
        white_number = white_tables[i + K - 1][j + K - 1] - white_tables[i - 1][j + K - 1] - white_tables[i + K - 1][j - 1] + white_tables[i - 1][j - 1]
        black_number = black_tables[i + K - 1][j + K - 1] - black_tables[i - 1][j + K - 1] - black_tables[i + K - 1][j - 1] + black_tables[i - 1][j - 1]
        result = min(result, white_number, black_number)

print(result)
