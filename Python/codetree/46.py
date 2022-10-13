import sys
from collections import deque
import math
N, M, K = list(map(int, sys.stdin.readline().strip().split()))

# 동북서남
dir_y = [0, -1, 0, 1]
dir_x = [1, 0, -1, 0]

blocks = [None] * N
for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))

heads = []


def out_of_range(y,x):
    return y < 0 or x < 0 or y >= N or x >= N

def get_head():
    for i in range(N):
        for j in range(N):
            if blocks[i][j] == 1:
                heads.append((i,j))


def find_tail(head_i, head_j):
    q = [(head_i, head_j)]
    visited = set((head_i, head_j))
    while q:
        r, c = q.pop()
        for i in range(4):
            next_r, next_c = r + dir_y[i], c + dir_x[i]
            if out_of_range(next_r, next_c) or (next_r, next_c) in visited:
                continue
            if blocks[next_r][next_c] == 2:
                q.append((next_r, next_c))
                visited.add((next_r, next_c))
            elif blocks[next_r][next_c] == 3:
                return next_r, next_c

def move(head_i, head_j, tail_i, tail_j):
    if abs(head_i - tail_i) + abs(head_j - tail_j) == 1:
        for i in range(4):
            next_tail_r, next_tail_c = tail_i + dir_y[i], tail_j + dir_x[i]
            if out_of_range(next_tail_r, next_tail_c):
                continue
            if blocks[next_tail_r][next_tail_c] == 2:
                blocks[next_tail_r][next_tail_c] = 3
        blocks[head_i][head_j], blocks[tail_i][tail_j] = 2, 1
    else:
        for i in range(4):
            next_head_r, next_head_c = head_i + dir_y[i], head_j + dir_x[i]
            if out_of_range(next_head_r, next_head_c):
                continue
            if blocks[next_head_r][next_head_c] == 4:
                blocks[next_head_r][next_head_c] = 1
                blocks[head_i][head_j] = 2
        for i in range(4):
            next_tail_r, next_tail_c = tail_i + dir_y[i], tail_j + dir_x[i]
            if out_of_range(next_tail_r, next_tail_c):
                continue
            if blocks[next_tail_r][next_tail_c] == 2:
                blocks[next_tail_r][next_tail_c] = 3
                blocks[tail_i][tail_j] = 4

def catch(direction, direction_count):
    if direction == 0: # 동
        for i in range(N):
            if blocks[direction_count][i] in (1,2,3):
                return direction_count, i
    elif direction == 1: # 북
        for i in range(N-1, -1, -1):
            if blocks[i][direction_count] in (1,2,3):
                return i, direction_count
    elif direction == 2: # 서
        for i in range(N-1, -1, -1):
            if blocks[N - direction_count - 1][i] in (1,2,3):
                return N - direction_count - 1, i
    else: # 남
        for i in range(N):
            if blocks[i][N - direction_count - 1] in (1,2,3):
                return i, N - direction_count - 1
    return -1, -1

def find_distance(i, j):
    q = [(i, j, 1)]
    visited = set((i, j))
    if blocks[i][j] == 1:
        return 1
    while q:
        r, c, count = q.pop()
        for i in range(4):
            next_r, next_c = r + dir_y[i], c + dir_x[i]
            if out_of_range(next_r, next_c) or (next_r, next_c) in visited:
                continue
            if blocks[next_r][next_c] == 2:
                q.append((next_r, next_c, count + 1))
                visited.add((next_r, next_c))
            if blocks[next_r][next_c] == 1 and blocks[r][c] != 3:
                return count + 1
    return 1
def changed_head(i, j):
    q = [(i, j, 0)]
    visited = set((i, j))
    head = (0,0)
    tail = (0,0)
    if blocks[i][j] == 1:
        head = (i,j)
    elif blocks[i][j] == 3:
        tail = (i,j)
    while q:
        r, c, count = q.pop()
        for i in range(4):
            next_r, next_c = r + dir_y[i], c + dir_x[i]
            if out_of_range(next_r, next_c) or (next_r, next_c) in visited:
                continue
            if blocks[next_r][next_c] == 2:
                q.append((next_r, next_c, count + 1))
            if blocks[next_r][next_c] == 1:
                head = (next_r, next_c)
            if blocks[next_r][next_c] == 3:
                tail = (next_r, next_c)
            visited.add((next_r, next_c))
    blocks[head[0]][head[1]], blocks[tail[0]][tail[1]] = blocks[tail[0]][tail[1]], blocks[head[0]][head[1]]

def solution():
    # get_head()
    # print(heads)
    # for b in blocks:
    #     print(b)
    # print()
    count, direction, direction_count = 0, 0, 0
    total = 0
    while count < K:
        # print("________________", count, "___________")
        # -------move
        get_head()
        while heads:
            head_i, head_j = heads.pop()
            tail_i, tail_j = find_tail(head_i, head_j)
            move(head_i, head_j, tail_i, tail_j)

        # for b in blocks:
        #     print(b)
        # print()
        #----------
        catched_i, catched_j = catch(direction, direction_count)
        if (catched_i, catched_j) != (-1, -1):
            score = find_distance(catched_i, catched_j)
            # print("catched", catched_i, catched_j, score)
            total += (score ** 2)
            changed_head(catched_i, catched_j)
        # print("catched postion", catched_i, catched_j)
        # print("catched", find_distance(catched_i, catched_j))

        # for b in blocks:
        #     print(b)
        # print()
        direction_count += 1
        if direction_count == N:
            direction = (direction + 1) % 4
            direction_count = 0
        count += 1

    return total

print(solution())

"""
7 2 1
3 2 1 0 0 0 0
4 0 4 0 2 1 4
4 4 4 0 2 0 4
0 0 0 0 3 0 4
0 0 4 4 4 0 4
0 0 4 0 0 0 4
0 0 4 4 4 4 4
"""