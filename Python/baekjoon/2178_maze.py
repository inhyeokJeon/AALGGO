import sys
from collections import defaultdict, deque

def main():
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    maze = [None] * n
    for _ in range(n):
        maze[_] = sys.stdin.readline().strip()
    visited = [[False] * m for _ in range(n)]

    dir_y = [-1, 0, 1, 0]
    dir_x = [0, 1, 0, -1]

    def out_of_range(y,x):
        return y < 0 or x < 0 or y >= n or x >= m

    def bfs(i,j):
        q = deque()
        q.append((i, j, 1))
        visited[i][j] = True
        count = 0
        ret = float("inf")
        while q:
            r, c, count = q.popleft()
            if r == (n - 1) and c == (m - 1):
                ret = min(ret, count)
            for d in range(4):
                next_r, next_c = r + dir_y[d], c + dir_x[d]
                if out_of_range(next_r, next_c) or visited[next_r][next_c]:
                    continue
                if maze[next_r][next_c] == "1":
                    q.append((next_r, next_c, count + 1))
                    visited[next_r][next_c] = True
        return ret
    print(bfs(0,0))


if __name__ == "__main__":
    main()
