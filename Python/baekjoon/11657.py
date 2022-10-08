import sys
from collections import defaultdict, Counter

N, M = list(map(int, sys.stdin.readline().strip().split()))

graph = defaultdict(list)
for _ in range(M):
    start, end, weight = list(map(int, sys.stdin.readline().strip().split()))
    graph[start].append((end, weight))
    # graph[end].append((start, weight))

def bel_for(start):
    distance = [float("INF")] * (N+1)
    distance[start] = 0
    # V-1 만큼 반복
    for _ in range(N-1):
        for node in sorted(graph):
            for next, next_weight in graph[node]:
                weight_sum = distance[node] + next_weight
                if distance[next] > weight_sum:
                    distance[next] = weight_sum

    for node in sorted(graph):
        for next, next_weight in graph[node]:
            weight_sum = distance[node] + next_weight
            if distance[next] > weight_sum:
                print(-1)
                return

    for i in range(2, len(distance)):
        if distance[i] == float("INF"):
            print(-1)
        else:
            print(distance[i])

bel_for(1)
