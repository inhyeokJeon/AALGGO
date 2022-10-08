import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())

distances = [[float("INF")] * N for _ in range(N)]

# for i in range(N):
#     distances[i][i] = 0

for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for idx, j in enumerate(temp):
        if j == 1:
            distances[i][idx] = 1
            # distances[idx][i] = 1


for k in range(N):
    for i in range(N):
        for j in range(N):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

for dd in distances:
    for d in dd:
        if d == float("INF"):
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()