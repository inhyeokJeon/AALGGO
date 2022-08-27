import sys
import heapq
from collections import deque
def solution():
    N, M = list(map(int, sys.stdin.readline().strip().split()))
    # matrix = [[0] for _ in range(M) for _ in range(N)]
    matrix = [[1] * (M + 2)]
    for i in range(N):
        X = []
        temp = sys.stdin.readline()
        for j in range(M):
            X.append(int(temp[j]))
        matrix.append([1] + X + [1])
    matrix.append([1] * (M + 2))
    # print(matrix)
    def dfs(i, j):
        dq = deque()
        dq.append([1, 1, i, j])
        # heapq.heappush(hq, (1, 1, i, j) )
        visited = [[[False,False] for _ in range(M+2)] for _ in range(N + 2)]
        visited[1][1][0] = True
        # print(visited)
        while dq:
            # print(dq)
            here_cost, can_break, here_y, here_x = dq.popleft()
            # heapq.heappop(hq)
            # print("here_cost, can_break, here_y, here_x :", here_cost, can_break, here_y, here_x)
            if here_y == N and here_x == M:
                return here_cost
                # print(N, M, here_cost)
                # break
            if visited[here_y][here_x][can_break]:
                continue
            visited[here_y][here_x][can_break] = True
            # print(visited)
            if here_y == 0 or here_x == 0 or here_y == N + 1 or here_x == M + 1:
                continue
            # 우
            if matrix[here_y][here_x + 1] == 0 and not visited[here_y][here_x + 1][can_break]:
                # print("RRR")
                dq.append((here_cost + 1, can_break, here_y, here_x + 1))
                # heapq.heappush(hq, (here_cost + 1, can_break, here_y, here_x + 1))
            # 벽뿌수고
            elif matrix[here_y][here_x + 1] == 1 and can_break > 0 and not visited[here_y][here_x + 1][can_break - 1]:
                # print("Break rRR")
                dq.append((here_cost + 1, can_break - 1, here_y, here_x + 1))
                # heapq.heappush(hq, (here_cost + 1, can_break - 1, here_y, here_x + 1))
            # 하
            if matrix[here_y + 1][here_x] == 0 and not visited[here_y + 1][here_x][can_break]:
                dq.append((here_cost + 1, can_break, here_y + 1, here_x))
                # heapq.heappush(hq, (here_cost + 1, can_break, here_y + 1, here_x))

            elif matrix[here_y + 1][here_x] == 1 and can_break > 0 and not visited[here_y + 1][here_x][can_break - 1]:
                dq.append((here_cost + 1, can_break - 1, here_y + 1, here_x))
                # heapq.heappush(hq, (here_cost + 1, can_break - 1, here_y + 1, here_x))

            # 좌
            if matrix[here_y][here_x - 1] == 0 and not visited[here_y][here_x - 1][can_break]:
                dq.append((here_cost + 1, can_break, here_y, here_x - 1))
                # heapq.heappush(hq, (here_cost + 1, can_break, here_y, here_x - 1))
            elif matrix[here_y][here_x - 1] == 1 and can_break > 0 and not visited[here_y][here_x - 1][can_break - 1]:
                dq.append((here_cost + 1, can_break - 1, here_y, here_x - 1))
                # heapq.heappush(hq, (here_cost + 1, can_break - 1, here_y, here_x - 1))
            # 상
            if matrix[here_y - 1][here_x] == 0 and not visited[here_y - 1][here_x][can_break]:
                dq.append((here_cost + 1, can_break, here_y - 1, here_x))
                # heapq.heappush(hq, (here_cost + 1, can_break, here_y - 1, here_x))
            elif matrix[here_y - 1][here_x] == 1 and can_break > 0 and not visited[here_y - 1][here_x][can_break - 1]:
                dq.append((here_cost + 1, can_break - 1, here_y - 1, here_x))
                # heapq.heappush(hq, (here_cost + 1, can_break - 1, here_y - 1, here_x))
        return -1

    print(dfs(1,1))


solution()



