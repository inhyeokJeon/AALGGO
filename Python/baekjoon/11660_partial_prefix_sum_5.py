import sys
from copy import deepcopy
N, M = list(map(int,sys.stdin.readline().strip().split()))
tables = [None] * (N + 1)
tables[0] = [0] * (N + 1)
for i in range(1, N + 1):
    tables[i] = [0] + list(map(int,sys.stdin.readline().strip().split()))


for i in range(1, N + 1):
    for j in range(1, N + 1):
        tables[i][j] += tables[i-1][j] + tables[i][j-1] - tables[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = list(map(int,sys.stdin.readline().strip().split()))
    print(tables[x2][y2] - tables[x1 - 1][y2] - tables[x2][y1 - 1] + tables[x1 - 1][y1 - 1])
