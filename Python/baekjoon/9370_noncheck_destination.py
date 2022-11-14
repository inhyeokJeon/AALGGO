import sys
import heapq
from collections import defaultdict

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, m, t = list(map(int, sys.stdin.readline().strip().split()))
        s, g, h = list(map(int, sys.stdin.readline().strip().split()))
        graph = defaultdict(dict)
        desinations = []

        for i in range(m):
            a, b, d = list(map(int, sys.stdin.readline().strip().split()))
            graph[a][b] = d
            graph[b][a] = d

        for i in range(t):
            desinations.append(int(sys.stdin.readline().strip()))

        def dijkstra(start):
            hq = []
            heapq.heappush(hq, (0, start))
            distance = [float("inf")] * (n + 1)
            distance[start] = 0
            while hq:
                count, node = heapq.heappop(hq)
                if distance[node] < count:
                    continue
                for next in graph[node]:
                    next_dist = count + graph[node][next]
                    if next_dist >= distance[next]:
                        continue
                    heapq.heappush(hq, (next_dist, next))
                    distance[next] = next_dist
            return distance
        # g h
        s_distances = dijkstra(s)
        g_distances = dijkstra(g)
        h_distances = dijkstra(h)
        for dest in sorted(desinations):
            original = s_distances[dest]
            if original == float("inf"):
                continue
            through = min(s_distances[g] + graph[g][h] + h_distances[dest],
                          s_distances[h] + graph[h][g] + g_distances[dest])
            if original == through:
                print(dest, end=" ")

if __name__ == "__main__":
    main()
