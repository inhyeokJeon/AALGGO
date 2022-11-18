# https://www.acmicpc.net/problem/1167
import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(dict)
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().strip().split()))
        for i in range(2, len(temp), 2):
            graph[temp[0]][temp[i -1]] = temp[i]

    total_max_val = 0
    def bfs(start):
        visited = [False] * (n + 1)
        dq = deque()
        dq.append((start, 0))
        max_number, max_num = start, 0
        visited[start] = True
        while dq:
            node, dist = dq.popleft()
            if max_num < dist:
                max_number = node
                max_num = dist
            for next in graph[node]:
                if not visited[next]:
                    dq.append((next, dist + graph[node][next]))
                    visited[next] = True
        return max_number, max_num
    last, distance = bfs(1)
    _, result = bfs(last)
    print(result)
if __name__ == "__main__":
    main()

"""
7
1 3 2 -1
2 4 4 -1
3 1 2 4 3 6 11 -1
4 2 4 3 3 5 6 7 20 -1
5 4 6 -1
6 3 11 -1
7 4 20 -1
"""
# 34
"""
2
1 2 4 -1
2 1 4 -1
"""

"""
4
1 2 4 3 5 4 6 -1
2 1 4 -1
3 1 5 -1
4 1 6 -1
"""