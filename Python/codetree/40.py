# 마주보는 면에 적혀있는 숫자의 합은 정확히 7입니다.
import sys

N, M = list(map(int, sys.stdin.readline().strip().split()))

# 동남서북
dir_y = [0, 1, 0, -1]
dir_x = [1, 0, -1, 0]
blocks = [None] * N
dice = [1, 2, 3] # 위 앞 오
position_y, position_x, number, direction = 0, 0, 6, 0  # 주사위 위치, 앞면 숫자 방향

for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))


def out_of_range(y,x):
    return y<0 or x<0 or y>=N or x>=N

def get_score(i,j):
    q = [(i,j)]
    visited = set()
    visited.add((i,j))
    count = 0
    while q:
        r, c = q.pop()
        # print("visited", r,c)
        count += 1
        for d in range(4):
            next_r, next_c = r + dir_y[d], c + dir_x[d]
            if out_of_range(next_r, next_c) or (next_r, next_c) in visited:

                continue
            if blocks[i][j] == blocks[next_r][next_c]:
                q.append((next_r, next_c))
                visited.add((next_r,next_c))
    return count * blocks[i][j]

def move():
    global position_x, position_y, direction, number, dice
    position_y, position_x = position_y + dir_y[direction], position_x + dir_x[direction]
    if direction == 0:
        number, dice = dice[2], [7 - dice[2], dice[1], dice[0]]
    elif direction == 1:
        number, dice = dice[1], [7 - dice[1], dice[0], dice[2]]
    elif direction == 2:
        number, dice = 7 - dice[2], [dice[2], dice[1], 7 - dice[0]]
    else:
        number, dice = 7 - dice[1], [dice[1], 7 - dice[0], dice[2]]

    if number > blocks[position_y][position_x]:
        direction = (direction + 1) % 4
    elif number < blocks[position_y][position_x]:
        direction = (direction - 1)
        if direction == -1:
            direction = 3

    temp_position_y, temp_position_x = position_y + dir_y[direction], position_x + dir_x[direction]
    if out_of_range(temp_position_y, temp_position_x):
        direction = (direction + 2) % 4

def solution():
    global position_x, position_y, direction, number, dice
    count = 0
    result = 0
    # print(position_y, position_x, direction, number, dice)
    while count < M:
        move()
        score = get_score(position_y, position_x)
        result += score
        # print(position_y, position_x, direction, number, dice, score)
        count += 1
    return result
print(solution())

"""inputs
4 20
1 2 4 4
4 2 2 2
5 2 6 6
5 3 3 1
"""