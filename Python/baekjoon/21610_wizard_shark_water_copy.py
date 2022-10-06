import sys
from copy import deepcopy
from collections import deque

dir_y = [0, -1, -1, -1, 0, 1, 1, 1] # 서쪽 부터 시계방향 8개
dir_x = [-1, -1, 0, 1, 1, 1, 0, -1]

diagonal_y = [-1, -1, 1, 1] # 좌상부터 시계방향
diagonal_x = [-1, 1, 1, -1]

N, M = list(map(int, sys.stdin.readline().strip().split()))

water_map = [[0] * N for _ in range(N)]
cloud_map = [[0] * N for _ in range(N)] # 구름은 1

magic = []
for i in range(N):
    water_map[i] = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
    magic.append(list(map(int, sys.stdin.readline().strip().split())))


# 4번 대각선방향으로만 물 복사할때만 사용
def out_of_range(y, x):
    return y < 0 or x < 0 or x >= N or y >= N

def move_cloud(index, cloud_list):
    direction, speed = magic[index]
    new_cloud_list = set()
    while cloud_list:
        cloud_y, cloud_x = cloud_list.pop()
        next_y, next_x = (cloud_y + (dir_y[direction - 1]) * speed) % N , (cloud_x + (dir_x[direction - 1]) * speed) % N
        new_cloud_list.add((next_y, next_x))
    return new_cloud_list

def solve():
    cloud_list = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]
    for i in range(M):
        moved_cloud = move_cloud(i, cloud_list) # 1
        for mr, mc in moved_cloud: # 2, 3
            water_map[mr][mc] += 1
        cand = []
        # 4
        for mr, mc in moved_cloud:
            count = 0
            for i in range(4):
                next_y, next_c = mr + diagonal_y[i], mc + diagonal_x[i]
                if out_of_range(next_y, next_c) or water_map[next_y][next_c] == 0: # 범위를 넘거나 물이 없으면
                    continue
                count += 1
            if count > 0:
                cand.append((mr, mc, count))
        for c_r, c_c, counter in cand:
            water_map[c_r][c_c] += counter
        # 5
        for i in range(N):
            for j in range(N):
                if water_map[i][j] < 2 or (i, j) in moved_cloud:
                    continue
                water_map[i][j] -= 2
                cloud_list.append((i,j))
        # print("------------after all step")
        # for w in water_map:
        #     print(w)
    # result
    all_sum = 0
    for i in range(N):
        all_sum += sum(water_map[i])

    print(all_sum)

solve()
"""input
5 4
0 0 1 0 2
2 3 2 1 0
4 3 2 9 0
1 0 2 9 0
8 8 2 1 0
1 3
3 4
8 1
4 8
"""
# ice_map = list(map(list, zip(*ice_map)))[::-1]
# for ice in ice_map:
#     print(ice)
# print(case)
