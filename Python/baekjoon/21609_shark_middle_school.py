"""
상어 중학교의 코딩 동아리에서 게임을 만들었다. 이 게임은 크기가 N×N인 격자에서 진행되고, 초기에 격자의 모든 칸에는 블록이 하나씩 들어있고, 블록은 검은색 블록, 무지개 블록, 일반 블록이 있다. 일반 블록은 M가지 색상이 있고, 색은 M이하의 자연수로 표현한다. 검은색 블록은 -1, 무지개 블록은 0으로 표현한다. (i, j)는 격자의 i번 행, j번 열을 의미하고, |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸 (r1, c1)과 (r2, c2)를 인접한 칸이라고 한다.

블록 그룹은 연결된 블록의 집합이다. 그룹에는 일반 블록이 적어도 하나 있어야 하며, 일반 블록의 색은 모두 같아야 한다. 검은색 블록은 포함되면 안 되고, 무지개 블록은 얼마나 들어있든 상관없다. 그룹에 속한 블록의 개수는 2보다 크거나 같아야 하며, 임의의 한 블록에서 그룹에 속한 인접한 칸으로 이동해서 그룹에 속한 다른 모든 칸으로 이동할 수 있어야 한다. 블록 그룹의 기준 블록은 무지개 블록이 아닌 블록 중에서 행의 번호가 가장 작은 블록, 그러한 블록이 여러개면 열의 번호가 가장 작은 블록이다.

오늘은 이 게임에 오토 플레이 기능을 만드려고 한다. 오토 플레이는 다음과 같은 과정이 블록 그룹이 존재하는 동안 계속해서 반복되어야 한다.

크기가 가장 큰 블록 그룹을 찾는다. 그러한 블록 그룹이 여러 개라면 포함된 무지개 블록의 수가 가장 많은 블록 그룹, 그러한 블록도 여러개라면 기준 블록의 행이 가장 큰 것을, 그 것도 여러개이면 열이 가장 큰 것을 찾는다.
1에서 찾은 블록 그룹의 모든 블록을 제거한다. 블록 그룹에 포함된 블록의 수를 B라고 했을 때, B2점을 획득한다.
격자에 중력이 작용한다.
격자가 90도 반시계 방향으로 회전한다.
다시 격자에 중력이 작용한다.
격자에 중력이 작용하면 검은색 블록을 제외한 모든 블록이 행의 번호가 큰 칸으로 이동한다. 이동은 다른 블록이나 격자의 경계를 만나기 전까지 계속 된다.
"""

import sys

# 서 북 남 동
dir = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def gravity(N, blocks):
    for i in range(N):
        # print("I행", i)
        start = N - 1
        end = N - 1
        while start >= end and end > -1:
            if blocks[start][i] == "#":
                # print("#", start, end)
                if blocks[end][i] == "#":
                    end -= 1
                elif blocks[end][i] == -1:
                    start = end - 1
                    end = end - 1
                else:
                    blocks[start][i], blocks[end][i] = blocks[end][i], blocks[start][i]
                    start -= 1
                    end -= 1
            else:
                # print("No #:", start, end)
                if blocks[end][i] == "#":
                    start = end
                    end -= 1
                elif blocks[end][i] == -1:
                    start = end - 1
                    end = end - 1
                else:
                    end -= 1
    return blocks

def del_visit(blocks, N, visited):
    for i in range(N):
        for j in range(N):
            if blocks[i][j] == 0:
                visited.discard((i,j))

def solve(blocks, N, M):
    answer = 0

    def counter_clock_wise(blocks):
        return list(map(list, zip(*blocks)))[::-1]


    def dfs(r, c, visited):

        if blocks[r][c] == "#" or blocks[r][c] == -1 or blocks[r][c] == 0 or (r,c) in visited:
            return set(), 0
        # print("왜이게되노", r,c, blocks[r][c])
        route = []
        stack = [(r,c)]
        # print("SETPOSITION", r, c)
        rainbow_count = 0
        while stack:
            now_r, now_c = stack.pop()
            if (now_r, now_c) in visited:
                continue
            # print("osition", now_r, now_c)
            # 무지개블록이면 체크 안함
            if blocks[now_r][now_c] == 0:
                rainbow_count += 1
            visited.add((now_r, now_c))
            route.append((now_r, now_c))
            for i in range(4):
                next_r, next_c = now_r + dir[i][0], now_c + dir[i][1]
                if (next_r, next_c) not in visited and 0 <= next_r < N and 0 <= next_c < N and (blocks[r][c] == blocks[next_r][next_c] or blocks[next_r][next_c] == 0) and blocks[r][c] != "#":
                    stack.append((next_r, next_c))

        return route, rainbow_count
    total = [None]


    while total:
        total = []
        now_max_length = float("-inf")
        visited = set()
        # print(total)
        for i in range(N):
            for j in range(N):
                route, rainbow = dfs(i, j, visited)
                del_visit(blocks, N, visited)
                if now_max_length <= len(route) and len(route) > 1:
                    now_max_length = len(route)
                    total.append([route, rainbow, (i, j)])

        if now_max_length < 2:
            break
        total.sort(key=lambda x: (len(x[0]), x[1], x[2]))
        # print("total:", total, now_max_length)
        # print(visited)
        # print()
        answer += (now_max_length**2)
        # for t in total[-1][0]:
        #     print(t)
        # print()
        for y, x in total[-1][0]:
            blocks[y][x] = "#"
        # for b in blocks:
        #     print(b)
        # print("after gravity")
        gravity(N, blocks)

        # for b in blocks:
        #     print(b)
        # print("after clock")
        blocks = counter_clock_wise(blocks)
        # for b in blocks:
        #     print(b)
        #
        # print("after gravity")
        gravity(N, blocks)
        # for b in blocks:
        #     print(b)
    return answer


def main():
    position = sys.stdin.readline().strip().split()
    N, M = int(position[0]), int(position[1])
    blocks = [None for _ in range(N)]
    for i in range(N):
        blocks[i] = list(map(int, sys.stdin.readline().strip().split()))

    print(solve(blocks, N, M))

main()
"""
5 3
2 2 -1 3 1
3 3 2 0 -1
0 0 0 1 2
-1 3 1 3 2
0 3 2 2 1

4 3
1 1 1 3
3 2 3 3
1 2 -1 3
-1 -1 1 1
33
"""

"""
5 3
0 0 0 0 1
-1 -1 0 -1 0
-1 -1 3 -1 -1
-1 -1 0 -1 -1
0 0 2 0 0
74

5 4
1 0 -1 0 0
2 0 -1 0 0
3 0 -1 0 0
4 0 -1 -1 -1
4 4 1 1 1
"""
# def gravity(N, blocks):
#     for i in range(N):
#         print("I행", i)
#         start = N - 1
#         end = N - 1
#         while start >= end and end > -1:
#             if blocks[start][i] == "#":
#                 print("#", start, end)
#                 if blocks[end][i] == "#":
#                     end -= 1
#                 elif blocks[end][i] == -1:
#                     start = end - 1
#                     end = end - 1
#                 else:
#                     blocks[start][i], blocks[end][i] = blocks[end][i], blocks[start][i]
#                     start -= 1
#                     end -= 1
#             else:
#                 print("No #:", start, end)
#                 if blocks[end][i] == "#":
#                     start = end
#                     end -= 1
#                 elif blocks[end][i] == -1:
#                     start = end - 1
#                     end = end - 1
#                 else:
#                     end -= 1
#     return blocks
# temp = [[2,2,-1,3,1], ["#", "#", 2, 0, -1], ["#", "#", "#", 1, 2], [-1, "#", 1, 3, 2], ["#", "#", 2, 2, 1]]
# gravity(5, temp)
#
# for t in temp:
#     print(t)
