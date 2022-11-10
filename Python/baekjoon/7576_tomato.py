import sys
from collections import deque


def main():
    # 북 동 남 서
    d_y = [-1, 0, 1, 0]
    d_x = [0, 1, 0, -1]
    m, n = list(map(int, sys.stdin.readline().strip().split()))
    tomatos = [None] * n
    goods = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        tomatos[i] = list(map(int, sys.stdin.readline().strip().split()))
        for j in range(m):
            if tomatos[i][j] == 1:
                goods.append((i, j, 0))
                visited[i][j] = True
            if tomatos[i][j] == -1:
                visited[i][j] = True
    def out_of_range(y,x):
        return y < 0 or x < 0 or y >= n or x >= m

    def bfs(good):
        q = deque(good)
        ans = float("-inf")
        while q:
            r, c, count = q.popleft()
            ans = max(ans, count)
            for d in range(4):
                next_r, next_c = r + d_y[d], c + d_x[d]
                if out_of_range(next_r, next_c) or visited[next_r][next_c]:
                    continue
                # if tomatos[next_r][next_c] == 0:
                q.append((next_r, next_c, count + 1))
                visited[next_r][next_c] = True
        return ans
    def final_check():
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    return False
        return True
    ans = bfs(goods)
    if final_check():
        print(ans)
    else:
        print(-1)

if __name__ == "__main__":
    main()
