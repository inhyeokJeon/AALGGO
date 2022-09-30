"""
4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 이후 물고기가 이동한다.

물고기는 번호가 작은 물고기부터 순서대로 이동한다. 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.
"""


import sys
from collections import deque
import heapq
from copy import deepcopy
# N, M = list(map(int, sys.stdin.readline().strip().split()))
block_first = [[0] * 4 for _ in range(4)]  # blocks
fish_dir = [(0,0), (-1,0), (-1,-1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fish_list = []
max_val = 0

for i in range(4):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(4):
        block_first[i][j] = (temp[j*2], temp[j*2+1])
        fish_list.append((temp[j*2], i, j, temp[j*2+1]))

fish_list.sort()

def out_of_range(y,x):
    return y < 0 or x < 0 or y >= 4 or x >= 4


def move_fish(blocks):
    count = 1
    while count < 17:
        check = False
        for i in range(4):
            for j in range(4):
                if blocks[i][j][0] == count:
                    r, c, n, d = i, j, blocks[i][j][0], blocks[i][j][1]
                    for _ in range(8): # 여덟 방향
                        next_r, next_c = r + fish_dir[d][0], c + fish_dir[d][1]
                        if out_of_range(next_r, next_c) or blocks[next_r][next_c][0] == "#":
                            d += 1
                            if d == 9:
                                d = 1
                            continue
                        blocks[r][c], blocks[next_r][next_c] = blocks[next_r][next_c], (blocks[r][c][0], d)

                        break
                    check = True
                if check:
                    break
            if check:
                break
        count += 1

def simulation(r, c, count, blockss):
    global max_val
    start_r, start_c, shark_dir = r, c, blockss[r][c][1]

    while True:
        cand = []
        for i in range(3):
            next_r, next_c = start_r + fish_dir[shark_dir][0], start_c + fish_dir[shark_dir][1]
            start_r, start_c = next_r, next_c
            if out_of_range(next_r, next_c) or blockss[next_r][next_c] == (0,0):
                continue
            cand.append((next_r, next_c, blockss[next_r][next_c][0], blockss[next_r][next_c][1]))
        if cand:
            for y, x, number, dir in cand:
                blockss[y][x] = ("#", dir)
                blockss[r][c] = (0,0)
                blocks = deepcopy(blockss)
                move_fish(blocks)
                simulation(y,x, count + number, blocks)
                max_val = max(max_val, count + number)
                blockss[r][c] = ("#", shark_dir)
                blockss[y][x] = (number, dir)
        else:
            break

def main():
    number = block_first[0][0][0]
    block_first[0][0] = ("#", block_first[0][0][1])
    move_fish(block_first)
    simulation(0, 0, number, block_first)
    print(max_val)

main()
"""
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2
"""