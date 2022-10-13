import sys
from collections import deque
from copy import deepcopy
N = int(sys.stdin.readline().strip())
blocks = [[] for _ in range(N)]
for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))

# 북쪽 부터 시계
dir_y = [-1, 0, 1, 0]
dir_x = [0, 1, 0, -1]


def out_of_range(x,y):
    return x < 0 or y < 0 or x >= N or y >= N


def counter_wise():
    global blocks
    blocks = list(map(list, zip(*blocks)))[::-1]


def clock_wise(temp):
    return list(map(list, zip(*temp[::-1])))


def cal_points(i, j, visited, groups) -> int:
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    number = blocks[i][j]
    score = 0
    while q:
        r, c = q.popleft()
        for d in range(4):
            next_r, next_c = r + dir_y[d], c + dir_x[d]
            if out_of_range(next_r, next_c) or visited[next_r][next_c]:
                continue
            if blocks[next_r][next_c] != number:
                score = score + (groups[next_r][next_c][1] + groups[r][c][1]) * groups[next_r][next_c][0] * groups[r][c][0]
                continue
            q.append((next_r, next_c))
            visited[next_r][next_c] = True

    return score


def grouping(i, j, visited, groups):
    q = deque()
    visited[i][j] = True
    q.append((i, j))
    number = blocks[i][j]
    point, count = 0, 0
    group = []
    while q:
        r, c = q.popleft()
        count += 1
        group.append((r,c))
        for d in range(4):
            next_r, next_c = r + dir_y[d], c + dir_x[d]
            if out_of_range(next_r, next_c) or visited[next_r][next_c] or blocks[next_r][next_c] != number:
                continue
            q.append((next_r, next_c))
            visited[next_r][next_c] = True

    for g_r, g_c in group:
        groups[g_r][g_c] = (number, count)



def count_points():
    all_points = 0
    visited = [[False] * N for _ in range(N)]
    groups = deepcopy(blocks)
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                grouping(i, j, visited, groups)

    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                all_points += cal_points(i, j, visited, groups)
    #
    # for group in groups:
    #     print(group)
    # print(all_points)
    return all_points

def split_four_clock_wise(copy_blocks, mid):
    # 좌상 우상 좌하 우하
    def first():
        temp = []
        for i in range(mid):
            temp.append(copy_blocks[i][:mid])
        temp = clock_wise(temp)
        return temp

    def second():
        temp = []
        for i in range(mid):
            temp.append(copy_blocks[i][mid+1:N])
        temp = clock_wise(temp)
        return temp

    def third():
        temp = []
        for i in range(mid+1, N):
            temp.append(copy_blocks[i][:mid])
        temp = clock_wise(temp)
        return temp

    def four():
        temp = []
        for i in range(mid+1, N):
            temp.append(copy_blocks[i][mid+1:N])
        temp = clock_wise(temp)
        return temp

    return first(), second(), third(), four()

def save_four_parts(one, two, three, four, mid):
    for i in range(mid):
        for j in range(mid):
            blocks[i][j] = one[i][j]

    for i in range(mid):
        for j in range(mid):
            blocks[i][j + mid + 1] = two[i][j]

    for i in range(mid):
        for j in range(mid):
            blocks[i + mid + 1][j] = three[i][j]

    for i in range(mid):
        for j in range(mid):
            blocks[i + mid + 1][j + mid + 1] = four[i][j]


def solution():
    total_points = 0
    total_points += count_points()
    for _ in range(3):
        mid = N // 2
        one, two, three, four = split_four_clock_wise(deepcopy(blocks), mid)
        counter_wise() # 블럭을 시계반대로 돌림.
        # 십자가 부분 제외하고 블럭에 4부분을 저장.
        save_four_parts(one, two, three, four, mid)
        points = count_points()
        total_points += points
    return total_points
print(solution())
