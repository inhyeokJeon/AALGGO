"""
크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다. 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나이다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.

이 도시에 사는 사람들은 치킨을 매우 좋아한다. 따라서, 사람들은 "치킨 거리"라는 말을 주로 사용한다. 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다. 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
"""

import sys

from collections import defaultdict, deque
# 서 북 남 동
dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]

position = sys.stdin.readline().strip().split()
N, M = int(position[0]), int(position[1])
blocks = [None for _ in range(N)]
chicken_count = 0
for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))

chicken = []
house = []
for i in range(N):
    for j in range(N):
        if blocks[i][j] == 2:
            chicken.append((i,j))
            chicken_count += 1
            # blocks[i][j] = 0
        if blocks[i][j] == 1:
            house.append((i,j))

answer = float("inf")
def out_ot_range(y, x): # 격자에서 벗어났는지 확인하는 함수
    return y < 0 or x < 0 or y >= N or x >= N

# def check_bfs(i, j, results):
#     q = deque()
#     q.append((i,j,0))
#     visited = set()
#     while q:
#         r, c, distance = q.popleft()
#         print("now position :  ",r,c)
#         if blocks[r][c] == 2:
#             results[(r,c)] = distance
#             print(i, j, "distance :", distance)
#             return distance
#         for d in range(4):
#             next_r, next_c = r + dir[d][0], c + dir[d][1]
#             if out_ot_range(next_r, next_c) or (next_r, next_c) in visited:
#                 continue
#             else:
#                 if results[(next_r, next_c)] > 0:
#                     return results[(next_r, next_c)] + distance
#                 q.append((next_r, next_c, distance + 1))
#                 visited.add((next_r, next_c))
#     # print("WHAT?")
#     return 0

def dfs(comb, depth):
    global answer
    if len(comb) == M:
        sum = 0
        for home_y, home_x in house:
            chicken_distance = float("inf")
            for i in range(M):
                chicken_y, chicken_x = chicken[comb[i]]
                chicken_distance = min(chicken_distance, abs(chicken_y - home_y) + abs(chicken_x - home_x))
            sum += chicken_distance

        # for i in range(M):
        #     y, x = chicken[comb[i]]
        #     blocks[y][x] = 2
        # # do do do do
        # # print(comb)
        #
        # sum = 0
        # results = defaultdict(int)
        # for i in range(N):
        #     for j in range(N):
        #         if blocks[i][j] == 1:

                    # sum += check_bfs(i, j, results)
        # for block in blocks:
        #     print(block)
        # print(sum)
        answer = min(answer, sum)

        for i in range(M):
            y, x = chicken[comb[i]]
            blocks[y][x] = 0
        return
    elif depth == chicken_count:
        return
    comb.append(depth)
    dfs(comb, depth + 1)
    comb.pop()
    dfs(comb, depth + 1)
def solve():
    comb = []
    # print(chicken)
    # print(chicken_count)
    dfs(comb, 0)
    print(answer)

solve()

"""
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

10
"""