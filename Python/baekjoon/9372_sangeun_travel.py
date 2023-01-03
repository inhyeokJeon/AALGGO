import sys
from collections import defaultdict, deque

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, m = list(map(int, sys.stdin.readline().strip().split()))
        graph = defaultdict(list)
        for _ in range(m):
            u, v = list(map(int, sys.stdin.readline().strip().split()))
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * (n + 1)
        def bfs(start):
            dq = deque()
            dq.append(start)
            visited[start] = True
            count = 0
            while dq:
                node = dq.popleft()
                count += 1
                for next in graph[node]:
                    if visited[next]:
                        continue
                    dq.append(next)
                    visited[next] = True
            return count
        print(bfs(1) - 1)


if __name__ == "__main__":
    main()

"""
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5
"""