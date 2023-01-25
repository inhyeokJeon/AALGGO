import heapq
import sys
from collections import defaultdict, deque
import math


def main():
    graph = defaultdict(list)
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    visited = set()
    connected = set()
    cand = [None] * (n + 1)
    hq = []
    for i in range(n):
        x1, y1 = list(map(int, sys.stdin.readline().strip().split()))
        cand[i + 1] = (x1, y1)

    for i in range(m):
        s1, s2 = list(map(int, sys.stdin.readline().strip().split()))
        connected.add(s1)
        connected.add(s2)
        # if s1 < s2:
        #
        # else:
        #     connected.add((s2, s1))

    for i in range(1, n):
        for j in range(i + 1, n + 1):
            first_x, first_y = cand[i]
            second_x, second_y = cand[j]
            heapq.heappush(hq, (math.sqrt((first_x - second_x) ** 2 + (first_y - second_y) ** 2), i, j))

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    def find(x): # find parent
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x < y:
            parent[x] = y
        else:
            parent[y] = x
        return
    answer = 0
    while hq:
        weight, node1, node2 = heapq.heappop(hq)
        if node1 in connected and node2 in connected:
            continue
        if find(node1) == find(node2):
            continue
        union(node1, node2)
        answer += weight

    print(answer)

if __name__ == "__main__":
    main()

"""
4 1
1 1
3 1
2 3
4 3
1 4
"""