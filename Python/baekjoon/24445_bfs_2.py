import sys
from collections import defaultdict, deque

def main():
    n, m, r = list(map(int, sys.stdin.readline().strip().split()))
    graph = defaultdict(list)
    visited = [0] * (n + 1)
    for _ in range(m):
        i, j = list(map(int, sys.stdin.readline().strip().split()))
        graph[i].append(j)
        graph[j].append(i)

    for key in graph:
        graph[key].sort(reverse=True)

    # print(graph)
    def bfs(start):
        q = deque()
        q.append(start)
        count = 1
        visited[start] = count
        while q:
            node = q.popleft()
            for next in graph[node]:
                if not visited[next]:
                    count += 1
                    visited[next] = count
                    q.append(next)

    bfs(r)
    for i in visited[1:]:
        print(i)




if __name__ == "__main__":
    main()

"""
5 5 1
1 4
1 2
2 3
2 4
3 4
"""