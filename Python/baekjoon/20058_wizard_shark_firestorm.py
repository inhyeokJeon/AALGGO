import sys
from copy import deepcopy
from collections import deque

dir_y = [0, 1, 0, -1] # 서 남 동 북
dir_x = [-1, 0, 1, 0]
N, Q = list(map(int, sys.stdin.readline().strip().split()))
width = 2 ** N
ice_map = [[0] * width for _ in range(width)]
case = None
# def slicing():
for i in range(width):
    ice_map[i] = list(map(int, sys.stdin.readline().strip().split()))

case = list(map(int, sys.stdin.readline().strip().split()))


def out_of_range(y, x):
    return y < 0 or x < 0 or x >= width or y >= width


# 범위를 나누고 회전
def rotate45(start_y, start_x, size):
    temp_map = []
    y = start_y
    for _ in range(size):
        temp_map.append(ice_map[y][start_x:start_x + size])
        y += 1
    # if size == 4:
    #     print("start", start_y, start_x)
    #     for t in temp_map:
    #         print(t)
    for i in range(size):
        for j in range(size):
            ice_map[i + start_y][j + start_x] = temp_map[size - j - 1][i]


def check(r, c):
    count = 0
    for i in range(4):
        next_r, next_c = r + dir_y[i], c + dir_x[i]
        if out_of_range(next_r, next_c) or ice_map[next_r][next_c] == 0: # 범위 벗어나거나 얼음이 없거나
            continue
        count += 1
    return count < 3

visited = [[False] * width for _ in range(width)]

def dfs(i, j):
    count = 0
    visited[i][j] = True
    q = deque()
    q.append((i,j))
    while q:
        r, c = q.popleft()
        count += 1
        for i in range(4):
            next_r, next_c = r + dir_y[i], c + dir_x[i]
            if out_of_range(next_r, next_c) or visited[next_r][next_c] or ice_map[next_r][next_c] == 0:
                continue
            q.append((next_r, next_c))
            visited[next_r][next_c] = True
    return count

def solve():

    for idx, test in enumerate(case):
        ice_sum = 0
        max_ice = 0
        # print(test)
        two_pow = 2 ** test
        # 범위를 나누고 회전
        for i in range(0, width, two_pow):
            for j in range(0, width, two_pow):
                rotate45(i, j, two_pow)
        # 주변 4방향 탐색 후 얼음이 3개 미만이면 -1
        cand = []
        for i in range(width):
            for j in range(width):
                if ice_map[i][j] == 0:
                    continue
                if check(i, j):
                    if ice_map[i][j] == 1:
                        cand.append((i,j))
                        continue
                    ice_map[i][j] -= 1
        for c_y, c_x in cand:
            ice_map[c_y][c_x] -= 1

    for i in range(width):
        for j in range(width):
            ice_sum += ice_map[i][j]
            if ice_map[i][j] == 0 or visited[i][j]:
                continue
            max_ice = max(max_ice, dfs(i, j))

    print(ice_sum)
    print(max_ice)
        # for ice in ice_map:
        #     print(ice)


solve()
# ice_map = list(map(list, zip(*ice_map[::-1]))) # 반시계
# copy_ice_map = deepcopy(ice_map)
# rotate45(2, 0, 2)

"""input
3 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8
8 7 6 5 4 3 2 1
1
"""
# ice_map = list(map(list, zip(*ice_map)))[::-1]
# for ice in ice_map:
#     print(ice)
# print(case)
