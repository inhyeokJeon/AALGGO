import sys


def solve():
    N = int(sys.stdin.readline().strip())

    six_field = []
    for _ in range(6):
        direction, length = list(map(int, sys.stdin.readline().strip().split()))
        six_field.append([direction,length])

    six_field += six_field
    for i in range(len(six_field) // 2):
        # ㄱ 남동남동북서
        if six_field[i][0] == 3 and six_field[i + 1][0] == 1 and \
                six_field[i + 2][0] == 3 and six_field[i + 3][0] == 1 and \
                six_field[i + 4][0] == 4 and six_field[i + 5][0] == 2:
            small = six_field[i + 1][1] * six_field[i + 2][1]
            big = six_field[i + 4][1] * six_field[i + 5][1]
            return N * (big - small)
        # 남동북동북서
        if six_field[i][0] == 3 and six_field[i + 1][0] == 1 and \
                six_field[i + 2][0] == 4 and six_field[i + 3][0] == 1 and \
                six_field[i + 4][0] == 4 and six_field[i + 5][0] == 2:
            small = six_field[i + 2][1] * six_field[i + 3][1]
            big = six_field[i][1] * six_field[i + 5][1]
            return N * (big - small)
        # 남동북서북서
        if six_field[i][0] == 3 and six_field[i + 1][0] == 1 and \
                six_field[i + 2][0] == 4 and six_field[i + 3][0] == 2 and \
                six_field[i + 4][0] == 4 and six_field[i + 5][0] == 2:
            small = six_field[i + 3][1] * six_field[i + 4][1]
            big = six_field[i][1] * six_field[i + 1][1]
            return N * (big - small)
        # 남동북서남서 # 왼쪽 맨위 (왼쪽먼저)
        if six_field[i][0] == 3 and six_field[i + 1][0] == 1 and \
                six_field[i + 2][0] == 4 and six_field[i + 3][0] == 2 and \
                six_field[i + 4][0] == 3 and six_field[i + 5][0] == 2:
            small = six_field[i + 4][1] * six_field[i + 5][1]
            big = six_field[i + 1][1] * six_field[i + 2][1]
            return N * (big - small)


print(solve())