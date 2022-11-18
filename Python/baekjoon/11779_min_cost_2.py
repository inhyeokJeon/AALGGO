# https://www.acmicpc.net/problem/11779
import sys
import heapq
from collections import defaultdict

def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(dict)
    for _ in range(m):
        start, end, cost = list(map(int, sys.stdin.readline().strip().split()))
        if end in graph[start].keys():
            graph[start][end] = min(graph[start][end], cost)
            continue
        graph[start][end] = cost


    start_point, dest_point = list(map(int, sys.stdin.readline().strip().split()))
    distance = [float("inf")] * (n + 1)
    def dijkstra(start):
        hq = []
        heapq.heappush(hq, (0, start, [start]))
        distance[start] = 0
        while hq:
            dist, node, route = heapq.heappop(hq)
            if distance[node] < dist:
                continue
            if node == dest_point:
                print(dist)
                print(len(route))
                print(*route)
                return
            for next in graph[node]:
                total = dist + graph[node][next]
                if distance[next] > total:
                    distance[next] = total
                    heapq.heappush(hq, (total, next, route + [next]))

    dijkstra(start_point)
    # print(distance)

if __name__ == "__main__":
    main()

