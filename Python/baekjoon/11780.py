import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

distances = [[float("INF")] * (N+1) for _ in range(N+1)]
trace = [[0] * (N+1) for _ in range(N+1)]


def find_path(i, j):
    if trace[i][j] == 0:
        return []
    k = trace[i][j]
    return find_path(i, k) + [k] + find_path(k, j)

for i in range(1, N+1):
    distances[i][i] = 0

for _ in range(M):
    start, end, weight = list(map(int, sys.stdin.readline().strip().split()))
    distances[start][end] = min(distances[start][end], weight)

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]
                trace[i][j] = k

for idx in range(1, len(distances)):
    for d in range(1, len(distances[idx])):
        if distances[idx][d] == float("INF"):
            print(0, end=" ")
        else:
            print(distances[idx][d], end=" ")
    print()

for i in range(1, N+1):
    for j in range(1, N+1):
        if distances[i][j] in (float("INF"), 0): # 자기 거나 못가면
            print(0)
            continue
        route = [i] + find_path(i,j) + [j]
        print(len(route), end=" ")
        print(*route)

