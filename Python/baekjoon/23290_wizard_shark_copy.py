"""
마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그, 비바라기, 블리자드 마법을 할 수 있다. 오늘은 기존에 배운 물복사버그 마법의 상위 마법인 복제를 배웠고, 4 × 4 크기의 격자에서 연습하려고 한다. (r, c)는 격자의 r행 c열을 의미한다. 격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (4, 4)이다.

격자에는 물고기 M마리가 있다. 각 물고기는 격자의 칸 하나에 들어가 있으며, 이동 방향을 가지고 있다. 이동 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다. 마법사 상어도 연습을 위해 격자에 들어가있다. 상어도 격자의 한 칸에 들어가있다. 둘 이상의 물고기가 같은 칸에 있을 수도 있으며, 마법사 상어와 물고기가 같은 칸에 있을 수도 있다.

상어의 마법 연습 한 번은 다음과 같은 작업이 순차적으로 이루어진다.

상어가 모든 물고기에게 복제 마법을 시전한다. 복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
모든 물고기가 한 칸 이동한다. 상어가 있는 칸, 물고기의 냄새가 있는 칸, 격자의 범위를 벗어나는 칸으로는 이동할 수 없다. 각 물고기는 자신이 가지고 있는 이동 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다. 물고기의 냄새는 아래 3에서 설명한다.
상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다. 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.
두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
격자에 있는 물고기의 위치, 방향 정보와 상어의 위치, 그리고 연습 횟수 S가 주어진다. S번 연습을 모두 마쳤을때, 격자에 있는 물고기의 수를 구해보자.
"""

import sys
from collections import defaultdict, Counter
from copy import deepcopy
# 서 북 동 남 45까지 포함 8개
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 북 서 남 동
dir_shark =[(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)]

temp = sys.stdin.readline().strip().split()
M, S = int(temp[0]), int(temp[1])
smell_blocks = [[0] * 5 for _ in range(5)]
blocks = [[0] * 5 for _ in range(5)]
# fish_dict_list = defaultdict(list)
fish_counter = Counter()
for _ in range(M):
    fish_y, fish_x, fish_dir = list(map(int,sys.stdin.readline().strip().split()))
    # fish_dict_list[(fish_y, fish_x)].append(fish_dir)
    # fish_list.append((fish_y, fish_x, fish_dir))
    fish_counter[(fish_y, fish_x, fish_dir)] += 1
    # blocks[fish_y][fish_x] = 0 # 이동 가능 공간.

shark_y, shark_x = list(map(int,sys.stdin.readline().strip().split()))

blocks[shark_y][shark_x] = -10

def out_of_range(y, x):
    return y < 1 or x < 1 or y >= 5 or x >= 5

def product(*args, repeat):
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]

    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for r in result:
        yield tuple(r)

def move_fish(): # 2번
    new_fish_counter = Counter()
    for fy, fx, fd in fish_counter:
        fish_y, fish_x, fish_dir = fy, fx, fd
        check_moved = False
        for _ in range(8):
            next_y, next_x = fish_y + dir[fish_dir][0], fish_x + dir[fish_dir][1]
            # 범위 상어 냄새.
            if out_of_range(next_y, next_x) or blocks[next_y][next_x] == -1 or smell_blocks[next_y][next_x] != 0:
                fish_dir -= 1
                if fish_dir <= 0:
                    fish_dir = 8
                # print(next_y, next_x, fish_dir)
                continue
            # fish_list[i][0], fish_list[i][1], fish_list[i][2] = next_y, next_x, fish_dir
            new_fish_counter[(next_y, next_x, fish_dir)] += fish_counter[(fy, fx, fd)]
            check_moved = True
            break
        if not check_moved:
            print("changed", (fy, fx, fd))
            new_fish_counter[(fy, fx, fd)] += fish_counter[(fy, fx, fd)]
    return new_fish_counter

def solve():
    global shark_y
    global shark_x
    # old_dict_list = fish_dict_list
    # old_list = fish_list

    for time in range(1, S + 1): # 마법 한번
        # 상어 위치
        # 원래 fish counter
        # for b in blocks:
        #     print(b)
        tttt = deepcopy(fish_counter)
        moved_fish_counter = move_fish()
        if tttt == fish_counter:
            print("SAME")
        # print("first fish counter", fish_counter)
        #
        # temp = 0
        # for s in fish_counter.values():
        #     temp += 1
        # print(temp)


        # print("first moved fish counter", moved_fish_counter)
        # temp = [[0] * 5 for _ in range(5)]
        # print("------moved----------", shark_y, shark_x, time)
        # for y, x, d in moved_fish_counter:
        #     temp[y][x] += moved_fish_counter[(y,x,d)]
        # for t in temp:
        #     print(t)
        # print("------blocks-----------")
        # for b in blocks:
        #     print(b)
        # # print(shark_y, shark_x)
        # print("-----------------")
        # temp = 0
        # for s in moved_fish_counter.values():
        #     temp += 1
        # print(temp)
        best_shark_y, best_shark_x = shark_y, shark_x
        max_fishing = float("-inf")
        max_steps = set()
        for temp_dir in product(range(1, 5), repeat=3): # (111,112,113 ... 333)
            now_shark_y, now_shark_x = shark_y, shark_x
            visited = []
            steps = set()

            fishing = 0
            for i in range(3):
                next_y, next_x = now_shark_y + dir_shark[temp_dir[i]][0], now_shark_x + dir_shark[temp_dir[i]][1]
                # if temp_dir == (2,2,1):
                #     print(fishing, steps, temp_dir, (next_y, next_x), visited, shark_y, shark_x)
                if out_of_range(next_y, next_x) or (next_y, next_x) in visited:
                    break
                visited.append((next_y, next_x))

                for _ in range(1, 9):
                    if moved_fish_counter[(next_y, next_x, _)] > 0:
                        fishing += moved_fish_counter[(next_y, next_x, _)]
                        steps.add((next_y, next_x))

                now_shark_y, now_shark_x = next_y, next_x
                # print("temp, fishing", temp_dir, fishing)
                if i == 2 and max_fishing < fishing:
                    print("FIHSING", now_shark_y, now_shark_x, fishing, temp_dir)
                    best_shark_y, best_shark_x = now_shark_y, now_shark_x
                    max_steps = steps
                    max_fishing = fishing

        blocks[shark_y][shark_x] = 0
        shark_y, shark_x = best_shark_y, best_shark_x
        blocks[shark_y][shark_x] = -1

        for y, x in max_steps:
            smell_blocks[y][x] = time

        for i in range(1,5):
            for j in range(1,5):
                if time - smell_blocks[i][j] == 2:
                    smell_blocks[i][j] = 0

        # print("removedL", max_fishing)
        # print("steps", max_steps)
        # max_steps.add((shark_y, shark_x))
        for y, x in max_steps:
            for d in range(1, 9):
                moved_fish_counter[(y,x,d)] = 0

        shark_y, shark_x = best_shark_y, best_shark_x
        fish_counter.update(moved_fish_counter)

        # print("last fish counter", fish_counter)
        # print("--------finished---------")
        # temp = [[0] * 5 for _ in range(5)]
        # for y, x, d in fish_counter:
        #     temp[y][x] += fish_counter[(y,x,d)]
        # for t in temp:
        #     print(t)
        #
        # print("--------blocks---------")
        # for b in blocks:
        #     print(b)
        # print("----------------")
        # print("--------smells---------")
        # for s in smell_blocks:
        #     print(s)
        # print("----------------")
        # print(temp)
        # print("last moved fish counter", moved_fish_counter)
        # temp = 0
        # for s in moved_fish_counter.values():
        #     temp += s
        temp = 0
        for s in fish_counter.values():
            temp += s
        print(temp)


        #
        # print(len(fish_list), fish_list)
        # print(shark_y, shark_x)
        # # 물고기 이동 -> fish_list 에 물고기 좌표 추가
        # # new_dict_list = move_fish(old_dict_list)
        # # old_dict_list = new_dict_list
        # old_list = fish_list.copy()
        # new_list = move_fish(old_list)
        # # old_list = new_list
        # max_fish = float("-inf")
        # last_killed_fish = []
        # best_posiiton_y, best_position_x = shark_y, shark_x
        # for temp_dir in product(range(1, 5), repeat=3): # (111,112,113 ... 333)
        #     now_shark_y, now_shark_x = shark_y, shark_x
        #     fishing = 0
        #     killed_fish = []
        #     # print("temp_dir", temp_dir, now_shark_y, now_shark_x)
        #     visited = []
        #     for fy, fx, _ in new_list:
        #         if (now_shark_y, now_shark_x) == (fy, fx):
        #             killed_fish.append((fy, fx, _))
        #             fishing += 1
        #     for i in range(3):
        #         next_y, next_x = now_shark_y + dir_shark[temp_dir[i]][0], now_shark_x + dir_shark[temp_dir[i]][1]
        #         if out_of_range(next_y, next_x) or (next_y, next_x) in visited:
        #             break
        #         visited.append((next_y, next_x))
        #         for fy, fx, _ in new_list:
        #             if (next_y, next_x) == (fy, fx):
        #                 killed_fish.append((fy, fx, _))
        #                 fishing += 1
        #
        #         now_shark_y, now_shark_x = next_y, next_x
        #         print("next", next_y, next_x)
        #         if i == 2 and max_fish < fishing:
        #             print("FIHSING", now_shark_y, now_shark_x, fishing)
        #             best_posiiton_y, best_position_x = now_shark_y, now_shark_x
        #             last_killed_fish = killed_fish
        #             max_fish = fishing
        #
        # print("killed", last_killed_fish)
        # killed_smells = []
        # for y, x, dir in last_killed_fish:
        #     if (y,x) not in killed_smells:
        #         blocks[y][x] = -2
        #         killed_smells.append((y,x))
        #     new_list.remove((y,x,dir))
        #
        # for i in range(1,5):
        #     for j in range(1,5):
        #         blocks[i][j] += 1
        #         if blocks[i][j] > 0:
        #             blocks[i][j] = 0
        #
        # print("old", old_list)
        # print("new", new_list)
        # fish_list.clear()
        # fish_list += old_list + new_list
        # blocks[shark_y][shark_x] = 0
        # shark_y, shark_x = best_posiiton_y, best_position_x
        # blocks[shark_y][shark_x] = float("-inf")
        # print(len(fish_list), fish_list)
        # print(shark_y, shark_x)
        # blocks

def main():
    solve()
    return
print(main())
"""
5 3
4 3 5
1 3 5
2 4 2
2 1 6
3 4 4
4 2
"""



