# 로봇 청소기

"""
로봇 청소기가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 장소는 N×M 크기의 직사각형으로 나타낼 수 있으며, 1×1크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다. 청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북중 하나이다. 지도의 각 칸은 (r, c)로 나타낼 수 있고, r은 북쪽으로부터 떨어진 칸의 개수, c는 서쪽으로 부터 떨어진 칸의 개수이다.

로봇 청소기는 다음과 같이 작동한다.

현재 위치를 청소한다.
현재 위치에서 현재 방향을 기준으로 왼쪽방향부터 차례대로 탐색을 진행한다.
왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.
로봇 청소기는 이미 청소되어있는 칸을 또 청소하지 않으며, 벽을 통과할 수 없다.
"""

"""inputs 
첫째 줄에 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 50)

둘째 줄에 로봇 청소기가 있는 칸의 좌표 (r, c)와 바라보는 방향 d가 주어진다. d가 0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽을 바라보고 있는 것이다.

셋째 줄부터 N개의 줄에 장소의 상태가 북쪽부터 남쪽 순서대로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 빈 칸은 0, 벽은 1로 주어진다. 지도의 첫 행, 마지막 행, 첫 열, 마지막 열에 있는 모든 칸은 벽이다.

로봇 청소기가 있는 칸의 상태는 항상 빈 칸이다.
"""
"""
3 3
1 1 0
1 1 1
1 0 1
1 1 1
"""
import sys
from collections import deque
# 북 동 남 서
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def solve(house, visited, r, c, d, N, M):
    answer = 0
    def check(i, j) -> bool: # 갈수 있으면 벽이아니고 방문한적 없으면 간다.
        if not visited[i][j] and house[i][j] != 1 and 0 <= i < N and 0 <= j < M:
            return True
        return False

    def turn(dir) -> int: # 왼쪽으로 돈다.
        dir = dir + 1
        if dir > 3:
            dir = 0
        return dir

    q = deque()
    q.append((r,c,d))
    while q:
        now_r, now_c, now_d = q.pop() # now
        house[now_r][now_c] = "#"
        # for h in house:
        #     print(h)
        if not visited[now_r][now_c]:
            answer += 1
        visited[now_r][now_c] = True
        # print(now_r, now_c, now_d, answer)
        check_count = 0
        next_d = now_d
        for _ in range(4):
            next_r, next_c = now_r + dir[next_d][0], now_c + dir[next_d][1]
            # print("next", next_r, next_c, next_d)
            if check(next_r, next_c):
                # visited[next_r][next_c] = True
                q.append((next_r, next_c, next_d))
                check_count += 1
            next_d = turn(next_d)
        if check_count == 0 : # 네방향 모두 벽이거나 청소를 이미 한 경우
            if house[now_r - dir[now_d][0]][now_c - dir[now_d][1]] == 1:
                return answer
            q.append((now_r - dir[now_d][0], now_c - dir[now_d][1], now_d))

    return answer

def main():
    position = sys.stdin.readline().strip().split()
    N, M = int(position[0]), int(position[1])
    direction = sys.stdin.readline().strip().split()
    r, c, d = int(direction[0]), int(direction[1]), int(direction[2])
    house = [None for _ in range(N)]
    for i in range(N):
        house[i] = list(map(int, sys.stdin.readline().strip().split()))
    visited = [[False] * (M) for _ in range(N)]
    return solve(house, visited, r, c, d, N, M)

print(main())


