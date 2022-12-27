import sys
from collections import defaultdict, deque

def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    graph = defaultdict(set)
    visited = [False] * (n + 1)
    # parent = [i for i in range(n + 1)]
    # # union find
    # def find(x):
    #     if x == parent[x]:
    #         return x
    #     parent[x] = find(parent[x])
    #     return parent[x]
    #
    # def union(x, y):
    #     x = find(x)
    #     y = find(y)
    #     if x != y:
    #         parent[y] = x
    #
    # for i in range(m):
    #     check, a, b = list(map(int, sys.stdin.readline().strip().split()))
    #     if check == 1:
    #         union(a, b)
    if n == 0 or m == 0:
        print("YES")
        return
    def dfs(start):
        dq = deque()
        dq.append(start)
        visited[start] = True
        while dq:
            node = dq.popleft()
            for next in graph[node]:
                if visited[next]:
                    continue
                dq.append(next)
                visited[next] = True
    for i in range(1, n + 1):
        con = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(len(con)):
            if con[j] == 1:
                graph[i].add(j + 1)
                graph[j + 1].add(i)

    plan = list(map(int, sys.stdin.readline().strip().split()))

    dfs(plan[0])
    for temp in plan:
        if not visited[temp]:
            print("NO")
            return
    print("YES")
    # print(visited)
if __name__ == "__main__":
    main()

"""
5
5
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
5 3 2 3 4
"""