from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    answer = 0
    graph = defaultdict(list)
    cost = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                cost[i][j] = 0
    for u, v, w in fares:
        cost[u][v] = w
        cost[v][u] = w

    for k in range(1, 1 + n):
        for i in range(1, 1 + n):
            for j in range(1, 1 + n):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    min_val = float('inf')
    for i in range(1, n + 1):
        min_val = min(min_val, cost[i][a] + cost[i][b] + cost[s][i])
        # if min_val > cost[i][a] + cost[i][b] + cost[s][i]:
        #     min_val = cost[i][a] + cost[i][b] + cost[s][i]
        #     center = i
    return min_val
    # print(dp)
    # hq = []
    #     heapq.heappush(hq, (0,s))
    #     def shortest_path(start):
    #         # print(start)
    #         visited = [False] * (n + 1)
    #         q = []
    #         heapq.heappush(q, (0, start))
    #         while q:
    #             weight, here = heapq.heappop(q)
    #             if visited[here]:
    #                 continue
    #             visited[here] = True
    #             dp[start][here] = weight
    #             for next, next_weight in graph[here]:
    #                 heapq.heappush(q, (next_weight+ weight, next))
    #     min_val = float('inf')
    #     center = 0
    #     for i in range(1, n + 1):
    #         shortest_path(i)
    #         if min_val > dp[i][a] + dp[i][b] + dp[s][i]:
    #             min_val = dp[i][a] + dp[i][b] + dp[s][i]
    #             center = i

    #     print(center)
    # while hq:
    #     weight, here = heapq.heappop(hq)
    #     print(here, weight)
    #     if here == a:
    #         a = 0
    #     if here == b:
    #         b = 0
    #     if a == 0 and b == 0:
    #         return weight
    #     for next, next_weight in graph[here]:
    #         heapq.heappush(hq, (next_weight + weight, next))
