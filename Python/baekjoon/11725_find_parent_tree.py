# https://www.acmicpc.net/problem/11725
import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline().strip())
    graph = defaultdict(list)
    for _ in range(n-1):
        start, end = list(map(int, sys.stdin.readline().strip().split()))
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * (n + 1)
    heads = [0] * (n + 1)
    def bfs(start):
        q = deque()
        q.append(start)
        visited[start] = True
        while q:
            node = q.popleft()
            for next in graph[node]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    heads[next] = node

    bfs(1)
    for i in range(2, len(heads)):
        print(heads[i])

if __name__ == "__main__":
    main()

