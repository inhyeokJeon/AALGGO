import sys

# 북동남서
dir_y = [-1, 0, 1, 0]
dir_x = [0, 1, 0, -1]
# 대각선들 오른쪽 위부터 시계
diagonal_y = [-1, 1, 1, -1]
diagonal_x = [1, 1, -1, -1]

N, M, K, C = list(map(int, sys.stdin.readline().strip().split()))

trees = [None] * N
killer = [[0] * N for _ in range(N)]
for i in range(N):
    trees[i] = list(map(int, sys.stdin.readline().strip().split()))


def out_of_range(y,x):
    return y < 0 or x < 0 or y >= N or x >= N


def grow():
    for i in range(N):
        for j in range(N):
            if trees[i][j] > 0:
                count = 0
                for d in range(4):
                    next_i, next_j = i + dir_y[d], j + dir_x[d]
                    if out_of_range(next_i, next_j):
                        continue
                    if trees[next_i][next_j] > 0:
                        count += 1
                trees[i][j] += count

def spread():
    cand = []
    for i in range(N):
        for j in range(N):
            if trees[i][j] > 0:
                position = []
                for d in range(4):
                    next_i, next_j = i + dir_y[d], j + dir_x[d]
                    if out_of_range(next_i, next_j) or trees[next_i][next_j] != 0 or killer[next_i][next_j] > 0:
                        continue
                    position.append((next_i, next_j))
                if position:
                    cand.append((position, trees[i][j] // len(position)))

    for position, length in cand:
        for p_i, p_j in position:
            trees[p_i][p_j] += length

def kill():
    best_y, best_x = -1, -1
    best_score = 0
    for i in range(N):
        for j in range(N):
            if trees[i][j] <= 0:
                continue
            count = trees[i][j]
            for d in range(4):
                for power in range(1, K + 1):
                    next_i, next_j = i + (diagonal_y[d] * power), j + (diagonal_x[d] * power)
                    if out_of_range(next_i, next_j) or trees[next_i][next_j] <= 0:
                        break
                    count += trees[next_i][next_j]

            if best_score < count:
                best_y, best_x = i, j
                best_score = count

    trees[best_y][best_x] = 0
    killer[best_y][best_x] = C + 1
    for d in range(4):
        for power in range(1, K + 1):
            next_i, next_j = best_y + (diagonal_y[d] * power), best_x + (diagonal_x[d] * power)
            if out_of_range(next_i, next_j) or trees[next_i][next_j] == -1:
                break
            if trees[next_i][next_j] == 0:
                killer[next_i][next_j] = C + 1
                break
            trees[next_i][next_j] = 0
            killer[next_i][next_j] = C + 1

    return best_score

def disappear():
    for i in range(N):
        for j in range(N):
            if killer[i][j] > 0:
                killer[i][j] -= 1

def solution():
    count = 0
    year = 1

    while year <= M:
        # print(year)
        # for k in killer:
        #     print(k)
        # print()

        # for t in trees:
        #     print(t)
        # print()
        grow()
        spread()
        # for t in trees:
        #     print(t)
        # print()
        count += kill()
        # for t in trees:
        #     print(t)
        # print()

        disappear()
        year += 1
    return count
print(solution())

"""
5 4 4 5
1 0 0 -1 5 
0 0 -1 4 0 
0 0 5 4 0 
0 0 5 0 0 
2 0 -1 0 0
"""