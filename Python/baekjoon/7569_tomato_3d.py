import sys
from collections import deque


def main():
    # 앞 뒤 북 동 남 서  y x h
    direction = [(1, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1)]
    m, n, h = list(map(int, sys.stdin.readline().strip().split()))
    tomatos = []
    goods = []
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]


    for H in range(h):
        temp = []
        for i in range(n):
            temp.append(list(map(int, sys.stdin.readline().strip().split())))
            for j in range(m):
                if temp[i][j] == 1:
                    goods.append((H, i, j, 0))
                    visited[H][i][j] = True
                elif temp[i][j] == -1:
                    visited[H][i][j] = True

        tomatos.append(temp)

    # print(tomatos)
    # print(visited)
    def out_of_range(k, y, x):
        return y < 0 or x < 0 or k < 0 or y >= n or x >= m or k >= h

    def bfs(good):
        q = deque(good)
        ans = float("-inf")
        while q:
            k, r, c, count = q.popleft()
            ans = max(ans, count)
            for d in range(6):
                next_k, next_r, next_c = k + direction[d][0], r + direction[d][1], c + direction[d][2]
                if out_of_range(next_k, next_r, next_c) or visited[next_k][next_r][next_c]:
                    continue
                # if tomatos[next_r][next_c] == 0:
                q.append((next_k, next_r, next_c, count + 1))
                visited[next_k][next_r][next_c] = True
        return ans
    def final_check():
        for k in range(h):
            for i in range(n):
                for j in range(m):
                    if not visited[k][i][j]:
                        return False
        return True
    ans = bfs(goods)
    if final_check():
        print(ans)
    else:
        print(-1)
    # for v in visited:
    #     print(v)
if __name__ == "__main__":
    main()
