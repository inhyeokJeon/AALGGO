"""
인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다. 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 동시에 복제되며, 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.

연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
"""

import sys
# sys.setrecursionlimit(10000)
from collections import defaultdict, deque
# 서 북 남 동
dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]

position = sys.stdin.readline().strip().split()
N, M = int(position[0]), int(position[1])
blocks = [None for _ in range(N)]
from copy import deepcopy
for i in range(N):
    blocks[i] = list(map(int, sys.stdin.readline().strip().split()))

virus = []
room_count = 0
virus_count = 0
min_time = float("inf")
for i in range(N):
    for j in range(N):
        if blocks[i][j] == 2:
            virus.append((i,j))
            virus_count += 1
            # blocks[i][j] = 0
        if blocks[i][j] == 0:
            room_count += 1

def check(laboratory):
    for i in range(N):
        if laboratory[i].count(0) > 0:
            return False
    return True

def out_ot_range(y, x): # 격자에서 벗어났는지 확인하는 함수
    return y < 0 or x < 0 or y >= N or x >= N

def bfs(q):
    global min_time
    visited = set()
    total_room = 0
    while q:
        r, c, time = q.popleft()
        if blocks[r][c] == 0:
            total_room += 1
        if total_room == room_count:
            min_time = min(min_time, time)
        for d in range(4):
            next_r, next_c = r + dir[d][0], c + dir[d][1]
            # 범위, 방문, 벽이면 패쓰
            if out_ot_range(next_r, next_c) or (next_r, next_c) in visited or blocks[next_r][next_c] == 1:
                continue
            else:
                q.append((next_r, next_c, time + 1))
                visited.add((next_r, next_c))

def solve(comb, depth):
    # print(len(comb))
    if len(comb) == M:
        # print(comb)
        q = deque()
        for c in comb:
            q.append((virus[c][0], virus[c][1], 0))
        bfs(q)
        # do something
        return
    elif depth == virus_count:
        # print("virus_count", virus_count)
        return
    comb.append(depth)
    solve(comb, depth + 1)
    comb.pop()
    solve(comb, depth + 1)

def main():
    comb = []
    # print(M)
    solve(comb, 0)
    if min_time == float("inf"):
        return -1
    else:
        return min_time

print(main())