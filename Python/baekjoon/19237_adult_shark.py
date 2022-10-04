"""
청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다. 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
"""
import sys
from collections import defaultdict, deque
N, M, k = list(map(int, sys.stdin.readline().strip().split()))
shark_map = [[[] for _ in range(N)] for _ in range(N)]
smell_map = [[0] * N for _ in range(N)]
shark_position = defaultdict(set)
shark_priority = defaultdict(list)

dir_y = [0, -1, 1, 0, 0] # 북 남 서 동
dir_x = [0, 0, 0, -1, 1]

for i in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(N):
        if temp[j] != 0:
            shark_map[i][j].append((temp[j], 0))

first_dir = list(map(int, sys.stdin.readline().strip().split()))

for i in range(N):
    for j in range(N):
        if shark_map[i][j]:
            shark_map[i][j] = [(shark_map[i][j][0][0], first_dir[shark_map[i][j][0][0] - 1])]
            shark_position[shark_map[i][j][0][0]] = (i,j)

# 순서대로 북 남 서 동일때 우선순위
# i번째 상어가 j(북 남 서 동) 순서 일때 우선 순위
for i in range(M):
    for j in range(4):
        shark_priority[i+1].append(list(map(int, sys.stdin.readline().strip().split())))

def shark_make_smell():
    count = 0
    for i in range(N):
        for j in range(N):
            if shark_map[i][j]:
                count += 1
                smell_map[i][j] = [shark_map[i][j][0][0], k]

def out_of_range(y,x):
    return y < 0 or x < 0 or y >= N or x >= N

def manage_smell():
    for i in range(N):
        for j in range(N):
            if smell_map[i][j] != 0:
                smell_map[i][j][1] -= 1
                if smell_map[i][j][1] == 0:
                    smell_map[i][j] = 0

def move_shark():
    # 1초 동안 움직이는 상어들
    for shark_number in shark_position:
        r, c = shark_position[shark_number]
        cand = []
        is_no_smell = False
        first_shark_dir = shark_map[r][c][0][1]
        for dir in shark_priority[shark_number][first_shark_dir - 1]: # 우선순위대로 4번
            next_r, next_c = r + dir_y[dir], c + dir_x[dir]
            # 범위를 넘어가면
            if out_of_range(next_r, next_c):
                continue
            # 냄새가 있고 자기 냄새라면 후보군에 넣고 아니면 continue
            if smell_map[next_r][next_c] != 0:
                if smell_map[next_r][next_c][0] == shark_number:
                    cand.append((next_r, next_c, dir))
                else:
                    continue
            # 주위에 냄새가 없다 ㄱ ㄱ
            if smell_map[next_r][next_c] == 0:
                is_no_smell = True
                shark_map[next_r][next_c].append((shark_number, dir))
                shark_position[shark_number] = (next_r, next_c)
                shark_map[r][c] = []
                break

        if not is_no_smell:
            next_r, next_c, d = cand.pop(0)
            shark_map[next_r][next_c].append((shark_number, d))
            shark_position[shark_number] = (next_r, next_c)
            shark_map[r][c] = []


    # 냄새를 하나씩 줄여준다. -> 0이면 없앤다.
    manage_smell()
    # 상어가 있는 칸은 죽이거나 냄새를 만들어준다.
    for i in range(N):
        for j in range(N):
            if shark_map[i][j]:
                if len(shark_map[i][j]) > 1: # 두놈 이상이 겹친다면
                    shark_map[i][j].sort() # 정렬 후
                    best = [shark_map[i][j].pop(0)]
                    while shark_map[i][j]:
                        deleted = shark_map[i][j].pop()
                        shark_position.pop(deleted[0])
                    shark_map[i][j] = best
                    # 맨 앞놈 빼고 제거.
                smell_map[i][j] = [shark_map[i][j][0][0], k] # 냄새를 남긴다.


def solve():
    answer = -1
    shark_make_smell()
    count = 1
    while count <= 1000:
        move_shark()
        if len(shark_position) == 1:
            answer = count
            break
        count += 1
    return answer

print(solve())
"""input
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3
"""