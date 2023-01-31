import heapq
import sys
from collections import defaultdict, deque
import math
# import heapq


def main():
    graph = defaultdict(list)
    n = int(sys.stdin.readline().strip())
    cand = []
    for i in range(n):
        star1, star2 = list(map(float, sys.stdin.readline().strip().split()))
        cand.append((star1, star2))

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            first_x, first_y = cand[i]
            second_x, second_y = cand[j]
            graph[i].append((j, math.sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2)))
            graph[j].append((i, math.sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2)))

    def solve(start):
        hq = []
        heapq.heappush(hq, (0, start))
        visited = set()
        ans = 0
        while hq:
            weight, node = heapq.heappop(hq)
            if node in visited:
                continue
            ans += weight
            visited.add(node)
            for next, next_weight in graph[node]:
                if next in visited:
                    continue
                heapq.heappush(hq, (next_weight, next))
        return ans

    print(round(solve(0), 2))

if __name__ == "__main__":
    main()

"""
3
1.0 1.0
2.0 2.0
2.0 4.0
"""