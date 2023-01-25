import heapq
import sys
from collections import defaultdict, deque
# import heapq


def main():
    # chosen group
    chosen = []
    graph = defaultdict(list)
    V, E = list(map(int, sys.stdin.readline().strip().split()))
    # hq = []
    for i in range(E):
        u, v, w = list(map(int, sys.stdin.readline().strip().split()))
        graph[u].append((v, w))
        graph[v].append((u, w))

    def mst(start):
        hq = []
        heapq.heappush(hq, (0, start))
        visited = set()
        # visited.append(start)
        # chosen.append(start)
        ret = 0
        while hq:
            weight, node = heapq.heappop(hq)
            if node in visited:
                continue
            visited.add(node)
            # chosen.append(node)
            ret += weight
            # print("visit: ", node , " weight : ", weight, "visited : ", visited)

            for next, next_weight in graph[node]:
                if next in visited:
                    continue
                heapq.heappush(hq, (next_weight, next))

        return ret

    print(mst(1))

if __name__ == "__main__":
    main()

"""
3 3
1 2 1
2 3 2
1 3 3
"""