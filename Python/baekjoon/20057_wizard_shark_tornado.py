import sys
dir_y = [0, 1, 0, -1] # 서 남 동 북
dir_x = [-1, 0, 1, 0]

dir_w_y = [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0]
dir_w_x = [0, 0, -1, -1, -1, -1, -2, -2, -3, -2]

dir_s_y = [0, 0, 1, 1, 1, 1, 2, 2, 3, 2]
dir_s_x = [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0]

dir_e_y = [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0]
dir_e_x = [0, 0, 1, 1, 1, 1, 2, 2, 3, 2]

dir_n_y = [0, 0, -1, -1, -1, -1, -2, -2, -3, -2]
dir_n_x = [-1, 1, -2, 2, -1, 1, -1, 1, 0, 0]

N = int(sys.stdin.readline().strip())
tornado_map = [[0] * N for _ in range(N)]
for i in range(N):
    tornado_map[i] = list(map(int, sys.stdin.readline().strip().split()))
result = 0


def out_of_range(y, x):
    return y < 0 or x < 0 or x >= N or y >= N


def spread(r, c, d, sand): # 버려지는 양
    global result
    temp_y, temp_x = None, None
    if d == 0:
        temp_y, temp_x = dir_w_y, dir_w_x
    elif d == 1:
        temp_y, temp_x = dir_s_y, dir_s_x
    elif d == 2:
        temp_y, temp_x = dir_e_y, dir_e_x
    elif d == 3:
        temp_y, temp_x = dir_n_y, dir_n_x
    total_sand = 0 # 이번턴에서 나눠지는 양
    for i in range(10):
        ny, nx = r + temp_y[i], c + temp_x[i]
        if i == 0 or i == 1:
            temp_sand = int(sand * 0.01)
        elif i == 2 or i == 3:
            temp_sand = int(sand * 0.02)
        elif i == 4 or i == 5:
            temp_sand = int(sand * 0.07)
        elif i == 6 or i == 7:
            temp_sand = int(sand * 0.1)
        elif i == 8:
            temp_sand = int(sand * 0.05)
        else:
            temp_sand = sand - total_sand
        if out_of_range(ny, nx):
            result += temp_sand
        else:
            tornado_map[ny][nx] += temp_sand

        total_sand += temp_sand


def tornado():
    r, c = N // 2, N // 2
    direction, move_count = 0, 0
    dist = 1  # 갈 수 있는 거리
    while True:
        move_count += 1
        for _ in range(dist):
            next_r, next_c = r + dir_y[direction], c + dir_x[direction]
            if out_of_range(next_r, next_c):  # 종료
                return
            if tornado_map[next_r][next_c] != 0:
                spread(r, c, direction, tornado_map[next_r][next_c])

            tornado_map[next_r][next_c] = 0
            r, c = next_r, next_c

        direction = (direction + 1) % 4
        if move_count == 2:
            dist += 1
            move_count = 0

def solve():

    tornado()
    return result
print(solve())

"""input
5
0 0 0 0 0
0 0 0 0 0
0 10 0 0 0
0 0 0 0 0
0 0 0 0 0
"""