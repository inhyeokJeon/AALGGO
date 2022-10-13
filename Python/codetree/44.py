# 이때 1 좌우로 움직이는 사람은 항상 오른쪽을 보고 시작하며, 2 상하로 움직이는 사람은 항상 아래쪽을 보고 시작합니다.
import sys
from collections import Counter
# 북 동 남 서
dir_y = [-1, 0, 1, 0]
dir_x = [0, 1, 0, -1]

# 리버스
# 남 동 북 서
r_dir_y = [1, 0, -1, 0]
r_dir_x = [0, 1, 0, -1]

N, M, H, K = list(map(int, sys.stdin.readline().strip().split()))
people = [[Counter() for _ in range(N)] for _ in range(N)]
trees = [[False] * N for _ in range(N)]
check_it = [[0] * N for _ in range(N)]
for _ in range(M):
    y, x, d = list(map(int, sys.stdin.readline().strip().split()))
    if d == 1:
        people[y-1][x-1][1] += 1
    else:
        people[y-1][x-1][2] += 1

for _ in range(H):
    y, x = list(map(int, sys.stdin.readline().strip().split()))
    trees[y-1][x-1] = True

def out_of_range(y, x):
    return y<0 or x<0 or y>=N or x>=N


def distance_in_3(y,x,p_y,p_x):
    return (abs(p_y-y) + abs(p_x-x)) <= 3

def move_people(y,x):
    # input 술래 좌표
    movement = []
    for i in range(N):
        for j in range(N):
            if people[i][j] and distance_in_3(y,x,i,j):
                temp = []
                for d in people[i][j]:
                    direction = d
                    next_i, next_j = i + dir_y[direction], j + dir_x[direction]
                    if out_of_range(next_i, next_j):
                        direction = (direction + 2) % 4
                    next_i, next_j = i + dir_y[direction], j + dir_x[direction]
                    if (next_i, next_j) == (y,x): # 술래가 잇으면 가지않는다.
                        continue
                    # print("move", i, j, "to the", next_i, next_j)
                    movement.append((next_i, next_j, direction, people[i][j][d]))
                    temp.append((i,j,d))
                for t_i, t_j, t_d in temp:
                    del people[t_i][t_j][t_d]

    for i, j, d, num in movement:
        people[i][j][d] += num


def kill(r,c, d_y, d_x):
    temp_r, temp_c = r, c
    number = 0
    # print("술래", r,c)
    for i in range(3):  # 3방향 본다.
        if out_of_range(temp_r, temp_c):
            break
        if trees[temp_r][temp_c]:
            temp_r, temp_c = temp_r + d_y, temp_c + d_x
            continue
        # print("술래", temp_r, temp_c, d_y, d_x)
        # 도망자 위치에 술래가 있으면 모든놈 잡는다.
        if people[temp_r][temp_c]:
            for direction in people[temp_r][temp_c]:
                number += people[temp_r][temp_c][direction]
            people[temp_r][temp_c].clear()
        temp_r, temp_c = temp_r + d_y, temp_c + d_x
    # print("몇명", number)
    return number

def tornado():
    # 토네이도 방향으로 하나씩
    r, c = N // 2, N // 2
    dir_count, dir, steps = 0, 0, 1
    count = 1
    score = 0
    reverse = False
    while count <= K:
        if not reverse:
            dir_count += 1
            # print(steps)
            for step in range(steps):
                # print("도둑은 여기", r, c)
                # print("steps", step, steps)
                # print("dir_count:", K, dir_count)
                next_r, next_c = r + dir_y[dir], c + dir_x[dir] # 술래는 움직인다.
                # print(next_r, next_c, dir)
                check_it[r][c] = count
                if (next_r, next_c) == (-1, 0):
                    # for check in check_it:
                    #     print(check)
                    dir = 0
                    r, c = 0, 0
                    dir_count = -1
                    steps = N-1
                    reverse = True
                    break
                if step == steps - 1:
                    dir = (dir + 1) % 4

                move_people(r, c)  # 도망자가 움직이고
                # for p in people:
                #     print(p)

                score += (count * kill(next_r, next_c, dir_y[dir], dir_x[dir]))  # 이동 직후 술래가 먼저 잡고
                count += 1
                if count == K + 1:
                    break
                # print("after catched")
                # for p in people:
                #     print(p)
                r, c = next_r, next_c

            if dir_count == 2:
                dir_count = 0
                # if not reverse:
                steps += 1
        else:
            # print("REVERSE MODE")
            dir_count += 1
            for step in range(steps):
                next_r, next_c = r + r_dir_y[dir], c + r_dir_x[dir]  # 술래는 움직인다.
                # print(r, c, steps)
                if step == steps - 1:
                    dir = (dir + 1) % 4
                move_people(r, c)  # 도망자가 움직이고
                # for p in people:
                #     print(p)
                check_it[r][c] = count
                score += (count * kill(next_r, next_c, r_dir_y[dir], r_dir_x[dir]))  # 이동 직후 술래가 먼저 잡고
                count += 1
                if count == K:
                    break
                # 도망자가 움직인다.
                # for p in people:
                #     print(p)
                # 술래와 거리가 3인 도망자만 움직인다.
                # todo
                r, c = next_r, next_c
            if dir_count == 2:
                dir_count = 0
                steps -= 1
                if steps == 0:
                    check_it[r][c] = count
                    # for check in check_it:
                    #     print(check)
                    dir = 0
                    reverse = False
                    dir_count = 0
                    steps = 1

    return score

print(tornado())

"""
5 24 9 100
3 4 1
5 1 2
3 2 1
5 4 1
5 2 1
1 2 2
2 4 1
4 3 2
4 1 2
4 2 1
2 1 1
1 5 1
3 1 2
2 2 1
1 4 1
4 4 1
4 5 2
3 5 1
5 3 1
2 3 2
5 5 2
1 3 1
2 5 1
1 1 1
1 1
1 5
3 2
3 1
4 1
5 5
5 1
2 4
2 5
"""