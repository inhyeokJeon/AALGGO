import sys
from collections import deque
from copy import deepcopy
N, M, K = list(map(int, sys.stdin.readline().strip().split()))
# 서 북 동 남
dir_y = [0, -1, 0, 1]
dir_x = [-1, 0, 1, 0]
# 서 북 동 남
air_dir = [[(0, -1), (1, -1), (-1, -1)], [(-1, 0), (-1, -1), (-1, 1)], [(0, 1), (-1, 1), (1, 1)], [(1, 0), (1, 1), (1, -1)]]
blocks = [None] * N
walls = [[[0, 0] for _ in range(N)] for _ in range(N)] # (위쪽, 왼쪽) 에 벽이 있다.
colds = [[0] * N for _ in range(N)]

offices = []
aircons = []
# 블록 등록
for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))
# 벽등록
for i in range(M):
    wall_y, wall_x, s = list(map(int, sys.stdin.readline().strip().split()))
    if s == 0:
        walls[wall_y - 1][wall_x - 1][0] = 1 # 위에 벽
    else:
        walls[wall_y - 1][wall_x - 1][1] = 1 # 왼쪽에 벽이 있따.

def out_of_range(y, x) -> bool:
    return y < 0 or x < 0 or y >= N or x >= N
def regist_office_aircon() -> None:
    for i in range(N):
        for j in range(N):
            if blocks[i][j] == 1:
                offices.append((i,j))
            elif blocks[i][j] >= 2:
                aircons.append((i,j,blocks[i][j] - 2))
def check_office() -> bool:
    for office_y, office_x in offices:
        if colds[office_y][office_x] < K:
            return False
    return True

def cooling():
    for air_y, air_x, direction in aircons:
        # print(air_y, air_x, direction)
        count = 5
        width = 1
        # 에어컨 바로 앞이 격자를 벗어나는 경우는 주어지지 않으며
        if direction == 0: # 서
            q = deque()
            q.append((air_y, air_x - 1, 5))
            visited = set()
            visited.add((air_y, air_x - 1))
            while q:
                r, c, count = q.popleft()
                colds[r][c] += count
                if count == 1:
                    continue
                for idx, (d_y, d_x) in enumerate(air_dir[direction]):
                    next_r, next_c = r + d_y, c + d_x
                    if idx == 0: # 직진
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c][1] == 1:
                            continue
                    elif idx == 1: # 직진에서 왼쪽
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r + 1][c][1] == 1 or walls[r+1][c][0] == 1:
                            continue
                    else: # 직진에서 오른쪽
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c][0] == 1 or walls[r-1][c][1] == 1:
                            continue
                    q.append((next_r, next_c, count - 1))
                    visited.add((next_r, next_c))
        elif direction == 1: # 북
            q = deque()
            q.append((air_y - 1, air_x, 5))
            visited = set()
            visited.add((air_y - 1, air_x))
            while q:
                r, c, count = q.popleft()
                colds[r][c] += count
                if count == 1:
                    continue
                for idx, (d_y, d_x) in enumerate(air_dir[direction]):
                    next_r, next_c = r + d_y, c + d_x
                    if idx == 0:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c][0] == 1:
                            continue
                    elif idx == 1:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c-1][0] == 1 or \
                                walls[r][c][1] == 1:
                            continue
                    else:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c + 1][1] == 1 or \
                                walls[r][c + 1][0] == 1:
                            continue
                    q.append((next_r, next_c, count - 1))
                    visited.add((next_r, next_c))
        elif direction == 2: # 동
            q = deque()
            q.append((air_y, air_x + 1, 5))
            visited = set()
            visited.add((air_y, air_x + 1))
            while q:
                r, c, count = q.popleft()
                colds[r][c] += count
                if count == 1:
                    continue
                for idx, (d_y, d_x) in enumerate(air_dir[direction]):
                    next_r, next_c = r + d_y, c + d_x
                    if idx == 0:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[next_r][next_c][1] == 1:
                            continue
                    elif idx == 1:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c][0] == 1 or \
                                walls[next_r][next_c][1] == 1:
                            continue
                    else:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r + 1][c][0] == 1 or \
                                walls[next_r][next_c][1] == 1:
                            continue
                    q.append((next_r, next_c, count - 1))
                    visited.add((next_r, next_c))
        else: # 남
            q = deque()
            q.append((air_y + 1, air_x, 5))
            visited = set()
            visited.add((air_y + 1, air_x))
            while q:
                r, c, count = q.popleft()
                colds[r][c] += count
                if count == 1:
                    continue
                for idx, (d_y, d_x) in enumerate(air_dir[direction]):
                    next_r, next_c = r + d_y, c + d_x
                    if idx == 0:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[next_r][next_c][0] == 1:
                            continue
                    elif idx == 1:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c + 1][1] == 1 or \
                                walls[next_r][next_c][0] == 1:
                            continue
                    else:
                        if out_of_range(next_r, next_c) or (next_r, next_c) in visited or walls[r][c][1] == 1 or \
                                walls[next_r][next_c][0] == 1:
                            continue
                    q.append((next_r, next_c, count - 1))
                    visited.add((next_r, next_c))

def shake_shake():
    cand = []
    for i in range(N):
        for j in range(N):
            if colds[i][j] != 0:
                for d in range(4):
                    next_i, next_j = i + dir_y[d], j + dir_x[d]
                    if d == 0: # 서북동남
                        if out_of_range(next_i, next_j) or walls[i][j][1] == 1:
                            continue
                    elif d == 1:
                        if out_of_range(next_i, next_j) or walls[i][j][0] == 1:
                            continue
                    elif d == 2:
                        if out_of_range(next_i, next_j) or walls[next_i][next_j][1] == 1:
                            continue
                    else:
                        if out_of_range(next_i, next_j) or walls[next_i][next_j][0] == 1:
                            continue
                    if (colds[i][j] - colds[next_i][next_j]) // 4 > 0:
                        cand.append((i,j, -((colds[i][j] - colds[next_i][next_j]) // 4) ))
                        cand.append((next_i, next_j, ((colds[i][j] - colds[next_i][next_j]) // 4)))

    for i, j, cold in cand:
        colds[i][j] += cold

def outer_line():
    for i in range(N):
        for j in range(N):
            if i == 0 or i == (N - 1) or j == 0 or j == (N-1):
                if colds[i][j] >= 1:
                    colds[i][j] -= 1

def solution():
    regist_office_aircon()
    count = 1
    # cooling()
    # temp = deepcopy(colds)
    while True:
        cooling()
        # print("after cooling")
        # for cold in colds:
        #     print(cold)
        shake_shake()
        # print("after shake")
        # for cold in colds:
        #     print(cold)
        outer_line()
        # print("after", count, "step")
        # for cold in colds:
        #     print(cold)
        # for t in temp:
        #     print(t)
        if check_office():
            break
        if count == 100:
            return -1
        # break
        count += 1
    return count
print(solution())


"""inputs
9 2 2
0 0 0 0 0 0 0 0 0 
0 0 1 1 1 0 0 0 0
0 0 1 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
4 8 1
5 8 1
"""

"""inputs
3 0 2
0 0 0
0 0 0
0 0 0
"""

"""inputs
5 4 10
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 3 0 0
3 3 0
3 3 1
4 3 0
3 4 1
"""