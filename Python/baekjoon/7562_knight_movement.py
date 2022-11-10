import sys
from collections import deque


def main():
    T = int(sys.stdin.readline().strip())
    d_y = [-1, -2, -2, -1, 1, 2, 2, 1]
    d_x = [-2, -1, 1, 2, 2, 1, -1, -2]
    for _ in range(T):
        n = int(sys.stdin.readline().strip())  # 한변의 길이
        start_y, start_x = list(map(int, sys.stdin.readline().strip().split()))
        end_y, end_x = list(map(int, sys.stdin.readline().strip().split()))

        visited = [[False] * n for _ in range(n)]

        def out_of_range(y,x):
            return y < 0 or x < 0 or y >= n or x >= n

        def bfs(i, j):
            q = deque()
            q.append((i, j, 0))
            visited[i][j] = 0
            while q:
                r, c, count = q.popleft()
                if r == end_y and c == end_x:
                    return count
                for d in range(8):
                    next_r, next_c = r + d_y[d], c + d_x[d]
                    if out_of_range(next_r, next_c) or visited[next_r][next_c]:
                        continue
                    q.append((next_r, next_c, count + 1))
                    visited[next_r][next_c] = True
        print(bfs(start_y, start_x))


if __name__ == "__main__":
    main()
