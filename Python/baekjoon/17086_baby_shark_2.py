"""
N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

안전 거리가 가장 큰 칸을 구해보자.
"""

import sys
from collections import deque
N, M = list(map(int, sys.stdin.readline().strip().split()))
blocks = [[0] * M for _ in range(N)]  # blocks
dir = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))


def out_of_range(y,x):
    return y < 0 or x < 0 or y >= N or x >= M


def solve():
    max_val = float("-inf")
    for i in range(N):
        for j in range(M):
            if blocks[i][j] == 0:
                # bfs 시작
                q = deque()
                visited = set()
                q.append((i,j, 0))
                visited.add((i,j))
                dist = 0
                while q:
                    row, col, distance = q.popleft()
                    # print(row, col, distance)
                    if blocks[row][col] == 1:
                        dist = distance
                        break
                    for idx in range(8):
                        next_r, next_c = row + dir[idx][0], col + dir[idx][1]
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited:# or (next_r, next_c) in did_shark_test:
                            continue
                        q.append((next_r, next_c, distance + 1))
                        visited.add((next_r,next_c))
                max_val = max(max_val, dist)
    return max_val


def main():
    print(solve())


main()