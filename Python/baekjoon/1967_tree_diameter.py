# https://www.acmicpc.net/problem/1967
import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(dict)
    for _ in range(n-1):
        start, end, cost = list(map(int, sys.stdin.readline().strip().split()))
        graph[start][end] = cost
        graph[end][start] = cost


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
