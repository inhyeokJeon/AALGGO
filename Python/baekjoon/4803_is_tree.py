import sys
from collections import defaultdict, deque


def main():
    def solve(t, vertex, edges):
        graph = defaultdict(list)
        for _ in range(edges):
            a, b = list(map(int, sys.stdin.readline().strip().split()))
            graph[a].append(b)
            graph[b].append(a)

        num_tree = 0
        visited = [False] * (n + 1)

        def bfs(start):
            visited[start] = True
            dq = deque()
            dq.append(start)
            flag = True
            parent = defaultdict(int)
            while dq:
                node = dq.popleft()
                # traced.add(node)
                for next in graph[node]:
                    if parent[node] == next:
                        continue
                    if not visited[next]:
                        dq.append(next)
                        visited[next] = True
                        parent[next] = node
                        # print("OK", next)
                        continue
                    # print("false", node, next)
                    flag = False
            return flag

        for i in range(1, vertex + 1):
            if not visited[i]:
                if bfs(i):
                    num_tree += 1

        if num_tree > 1:
            print(f"Case {t}: A forest of {num_tree} trees.")
        elif num_tree == 1:
            print(f"Case {t}: There is one tree.")
        else:
            print(f"Case {t}: No trees.")


    T = 1
    while True:
        n, m = list(map(int, sys.stdin.readline().strip().split()))
        if n == 0 and m == 0:
            break
        solve(T, n, m)
        T += 1


if __name__ == "__main__":
    main()


"""
7 7
1 2
2 3
3 1
4 5
5 6
6 4
1 6
0 0
"""