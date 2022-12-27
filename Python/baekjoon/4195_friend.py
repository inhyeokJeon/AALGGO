import sys
from collections import defaultdict, deque

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        F = int(sys.stdin.readline().strip())
        graph = defaultdict(set)
        ret = defaultdict(int)
        # def dfs(start):
        #     visited = defaultdict(bool)
        #     dq = deque()
        #     dq.append(start)
        #     visited[start] = True
        #     count = 0
        #     while dq:
        #         node = dq.popleft()
        #         count += 1
        #         for next in graph[node]:
        #             if visited[next]:
        #                 continue
        #             dq.append(next)
        #             visited[next] = True
        #     return count
        parent = defaultdict(str)
        # union find
        def find(x):
            if parent[x] == "": # root 면
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if ret[x] == 0:
                ret[x] = 1
            if ret[y] == 0:
                ret[y] = 1
            if x != y:
                parent[y] = x
                ret[x] += ret[y]
                # print("union", x, ret[x], y, ret[y])
        for _ in range(F):
            f1, f2 = sys.stdin.readline().strip().split()
            if f1 < f2:
                union(f1, f2)
            else:
                union(f2, f1)
            print(ret[find(f1)])


if __name__ == "__main__":
    main()

"""
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

2
3
4
2
2
4
"""