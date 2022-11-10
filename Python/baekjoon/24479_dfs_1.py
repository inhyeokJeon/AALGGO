import sys
from collections import defaultdict

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
    def dfs(start):
        q = [start]
        count = 1
        while q:
            node = q.pop()
            if visited[node]:
                continue
            # print(node)
            visited[node] = count
            count += 1
            for next in graph[node]:
                if not visited[next]:
                    q.append(next)

    dfs(r)
    for i in visited[1:]:
        print(i)




if __name__ == "__main__":
    main()

"""
6 4 1
2 3
1 4
1 5
4 6
"""