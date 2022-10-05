import sys
from copy import deepcopy
from collections import defaultdict, deque

dir_y = [-1, -1, 0, 1, 1, 1, 0, -1]
dir_x = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = list(map(int, sys.stdin.readline().strip().split()))
fire_map = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = list(map(int, sys.stdin.readline().strip().split()))
    fire_map[r-1][c-1].append((m,s,d))

def move_fire():
    temp = []
    for i in range(N):
        for j in range(N):
            while fire_map[i][j]:
                m, s, d = fire_map[i][j].pop(0)
                next_r, next_c = (i + (dir_y[d] * s)) % N, (j + (dir_x[d] * s)) % N
                temp.append((next_r, next_c, m, s, d))

    while temp:
        n_r, n_c, n_m, n_s, n_d = temp.pop(0)
        fire_map[n_r][n_c].append((n_m, n_s, n_d))


def check_dir(dir_list):
    first_number = dir_list.pop()
    determ = first_number % 2
    while dir_list:
        d = dir_list.pop()
        if determ != d % 2:
            return [1,3,5,7]
    return [0, 2, 4, 6]


def check_more_two():
    temp = []
    for i in range(N):
        for j in range(N):
            if fire_map[i][j]:
                if len(fire_map[i][j]) > 1: # 두개이상의 파이어볼이 존재하면.
                    # 모두 합친다. 2-3의 규칙에 따라
                    length = len(fire_map[i][j])
                    sum_m = 0
                    sum_s = 0
                    dir_list = []
                    while fire_map[i][j]: # 하나로 합치고
                        m, s, d = fire_map[i][j].pop()
                        sum_m += m
                        sum_s += s
                        dir_list.append(d)
                    last_m = sum_m // 5
                    if last_m == 0:
                        continue
                    last_s = sum_s // length
                    cand_dir = check_dir(dir_list)
                    while cand_dir: # 네개로 나눈다.
                        d = cand_dir.pop(0)
                        temp.append((i, j, last_m, last_s, d))

    while temp:
        n_r, n_c, n_m, n_s, n_d = temp.pop(0)
        fire_map[n_r][n_c].append((n_m, n_s, n_d))

def cal_last_fire():
    sum_m = 0
    for i in range(N):
        for j in range(N):
            if fire_map[i][j]:
                while fire_map[i][j]:
                    n_m, _, _ = fire_map[i][j].pop()
                    sum_m += n_m
    return sum_m

def solve():
    answer = -1
    for _ in range(K):
        # print("original-----------------")
        # for f in fire_map:
        #     print(f)
        move_fire()
        # print("moved-----------------")
        # for f in fire_map:
        #     print(f)
        check_more_two()
        # print("after-----------------")
        # for f in fire_map:
        #     print(f)
    answer = cal_last_fire()
    return answer

print(solve())

"""input
4 2 1
1 1 5 2 2
1 4 7 1 6
"""