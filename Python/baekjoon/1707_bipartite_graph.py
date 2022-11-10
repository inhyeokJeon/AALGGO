import sys
from collections import deque, defaultdict

# 이분 그래프 -> 서로 다른 정점을 빨간색, 파란색 번갈아가면서 순회할 수 있는 그래프.
def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        V, E = list(map(int, sys.stdin.readline().strip().split()))
        visited = [False] * (V + 1)
        graph = defaultdict(list)
        for _ in range(E):
            start, end = list(map(int, sys.stdin.readline().strip().split()))
            graph[start].append(end)
            graph[end].append(start)

        def bfs(start):
            q = deque()
            q.append(start)
            visited[start] = 1
            while q:
                node = q.popleft()
                for next in graph[node]:
                    if not visited[next]:
                        q.append(next)
                        visited[next] = -1 * visited[node]
                    elif visited[node] == visited[next]:
                        return False
            return True

        ret = True
        for i in range(1, V + 1):
            if not visited[i]:
                if not bfs(i):
                    ret = False
                    break
        if ret:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()

"""
1
5 4
1 2
2 3
3 4
4 5
"""
