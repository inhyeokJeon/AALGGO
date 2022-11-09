import sys
dir_y = [-1, 0, 1, 0] # 북 동 남 서
dir_x = [0, 1, 0, -1]

sys.setrecursionlimit(10000)
def main():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    matrix = [None] * N
    for i in range(N):
        matrix[i] = list(map(int, sys.stdin.readline().strip().split()))
    visited = [[False] * M for _ in range(N)]
    result = [[0] * M for _ in range(N)]

    def out_of_range(y, x):
        return y < 0 or x < 0 or y >= N or x >= M

    # result -1 이 된 곳은 이미 가봤지만 결승점에 도달할 수 없던 곳,
    # result > 0 은 이미 가본 길 중 결승점에 도달 할 수 있던 길들
    # 이 두가지를 기억해 중복 행위를 제거한다. result 매트릭스에서
    def dfs(r, c):
        if r == N-1 and c == M-1:
            result[r][c] = 1

        for dir in range(4):
            next_r, next_c = r + dir_y[dir], c + dir_x[dir]
            if out_of_range(next_r, next_c) or visited[next_r][next_c] or result[next_r][next_c] == -1:
                continue

            if matrix[r][c] > matrix[next_r][next_c]:
                visited[next_r][next_c] = True
                if result[next_r][next_c] > 0:
                    result[r][c] += result[next_r][next_c]

                else:
                    dfs(next_r, next_c)
                    if result[next_r][next_c] > 0:
                        result[r][c] += result[next_r][next_c]
                    else:
                        result[r][c] == -1
                visited[next_r][next_c] = False
        if result[r][c] == 0:
            result[r][c] = -1

    visited[0][0] = True
    dfs(0, 0)

    # for r in result:
    #     print(r)
    if result[0][0] == -1:
        print(0)
    else:
        print(result[0][0])


if __name__ == "__main__":
    main()

"""inputs
4 5
50 45 37 32 30
35 50 17 20 25
30 17 20 17 28
27 24 22 15 10
"""

"""
4 5
50 45 37 32 30
35 50 40 20 25
30 21 25 17 28
27 24 22 15 10
"""

"""
2 2
1 2
2 1
"""