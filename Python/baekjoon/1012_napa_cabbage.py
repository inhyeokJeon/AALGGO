import sys
from collections import deque

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        m, n, k = list(map(int, sys.stdin.readline().strip().split()))
        maps = [[0] * m for _ in range(n)]
        for _ in range(k):
            i, j = list(map(int, sys.stdin.readline().strip().split()))
            maps[j][i] = 1
        visited = [[False] * m for _ in range(n)]
        total = 0
        # 북동남서
        dir_y = [-1, 0, 1, 0]
        dir_x = [0, 1, 0, -1]

        def out_of_range(y,x):
            return y < 0 or x < 0 or y >= n or x >= m

        def bfs(i,j):
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            count = 0
            while q:
                r, c = q.popleft()
                count += 1
                for d in range(4):
                    next_r, next_c = r + dir_y[d], c + dir_x[d]
                    if out_of_range(next_r, next_c) or visited[next_r][next_c]:
                        continue
                    if maps[next_r][next_c] == 1:
                        q.append((next_r, next_c))
                        visited[next_r][next_c] = True
            return count

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and maps[i][j] == 1:
                    total += 1
                    maps.append(bfs(i, j))

        print(total)


if __name__ == "__main__":
    main()

"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
"""