import sys
from collections import deque

tornado_y = [0, 1, 0, -1] # 서 남 동 북
tornado_x = [-1, 0, 1, 0]

dir_y = [-1, 1, 0, 0] # 북 남 서 동
dir_x = [0, 0, -1, 1]


N, M = list(map(int, sys.stdin.readline().strip().split()))

blizard_map = [[0] * N for _ in range(N)]

magic = []
for i in range(N):
    blizard_map[i] = list(map(int, sys.stdin.readline().strip().split()))

for i in range(M):
    magic.append(list(map(int, sys.stdin.readline().strip().split())))


# 4번 대각선방향으로만 물 복사할때만 사용
def out_of_range(y, x):
    return y < 0 or x < 0 or x >= N or y >= N


def blizard_magic(d, s):
    r, c = N // 2, N // 2
    for distance in range(1, s+1):
        n_r, n_s = r + (dir_y[d]) * distance, c + (dir_x[d]) * distance
        blizard_map[n_r][n_s] = 0


def remove_zero(extended: deque):
    new_list = deque()


    while extended:
        num = extended.popleft()
        if num != 0:
            new_list.append(num)
    return new_list

def delete_countinuous(extended: deque):
    start = 0
    end = 0
    is_continuous = False

    score = 0
    while start <= end and end < len(extended) and extended[end] != 0:
        if extended[start] == extended[end]:
            end += 1
            if end - start >= 4:
                is_continuous = True
        else:
            if is_continuous:
                score += ((end - start) * extended[start])
                for i in range(start, end):
                    extended[i] = 0

            start = end
            end += 1
            is_continuous = False

    if end - start >= 4:
        score += ((end - start) * extended[start])
        for i in range(start, end):
            extended[i] = 0

    return score


def to_group(extended: deque):
    result = deque()
    start = 0
    end = 1
    while start <= end and end < len(extended) and extended[end] != 0 and extended[start] != 0:

        if extended[start] == extended[end]: # grouping
            end += 1
        else:
            result.append(end - start)
            result.append(extended[start])
            start = end
            end += 1

    result.append(end - start)
    result.append(extended[start])
    return result


def extended_to_blizard_map(extended):
    r, c = N // 2, N // 2
    distance = 1
    move_count, direction = 0, 0
    result = [[0] * N for _ in range(N)]
    while True:
        move_count += 1
        for _ in range(distance):
            next_r, next_c = r + tornado_y[direction], c + tornado_x[direction]
            if (next_r, next_c) == (0, -1):
                return result
            if extended:
                result[next_r][next_c] = extended.popleft()
            else:
                result[next_r][next_c] = 0

            r, c = next_r, next_c
        direction = (direction + 1) % 4
        if move_count == 2:
            distance += 1
            move_count = 0

    return result
def make_extended_list():
    r, c = N // 2, N // 2
    distance = 1
    move_count, count, direction = 0, 0, 0
    result = deque()
    while True:
        move_count += 1
        for _ in range(distance):
            next_r, next_c = r + tornado_y[direction], c + tornado_x[direction]

            if (next_r, next_c) == (0, -1):
                return result

            if blizard_map[next_r][next_c] != 0:
                result.append(blizard_map[next_r][next_c])

            r, c = next_r, next_c
        direction = (direction + 1) % 4
        if move_count == 2:
            distance += 1
            move_count = 0


def solve():
    global blizard_map
    result = 0
    for d, s in magic:
        blizard_magic(d - 1, s)
        extended_tornado = make_extended_list()
        while True:
            score = delete_countinuous(extended_tornado) # 붐
            if score == 0:
                break
            else:
                result += score

            extended_tornado = remove_zero(extended_tornado)
        if not extended_tornado:
            break
        grouped = to_group(extended_tornado)
        blizard_map = extended_to_blizard_map(grouped)
    print(result)
solve()
"""
7 1
0 0 0 0 0 0 0
3 2 1 3 2 3 0
2 1 2 1 2 1 0
2 1 1 0 2 1 1
3 3 2 3 2 1 2
3 3 3 1 3 3 2
2 3 2 2 3 2 3
2 2
"""

"""
5 1
0 0 0 0 0
0 0 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0
1 2
"""