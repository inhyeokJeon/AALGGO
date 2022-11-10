import sys
from collections import deque

def main():
    n = int(sys.stdin.readline().strip())
    house = [None] * n
    for _ in range(n):
        house[_] = sys.stdin.readline().strip()
    visited = [[False] * n for _ in range(n)]
    total = 0
    house_count = []
    # 북동남서
    dir_y = [-1, 0, 1, 0]
    dir_x = [0, 1, 0, -1]

    def out_of_range(y,x):
        return y < 0 or x < 0 or y >= n or x >= n

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
                if house[next_r][next_c] == "1":
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = True
        return count

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and house[i][j] == "1":
                total += 1
                house_count.append(bfs(i, j))
    house_count.sort()
    print(total)
    for h in house_count:
        print(h)


if __name__ == "__main__":
    main()

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""