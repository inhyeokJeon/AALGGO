import sys

N = int(sys.stdin.readline().strip())


def solve():
    stairs = [[0] * 10 for _ in range(N + 1)]
    if N == 1:
        return 9
    if N == 2:
        return 17
    for i in range(1, 10):
        stairs[1][i] = 1

    for i in range(2, N + 1):
        stairs[i][0] = stairs[i - 1][1]
        for j in range(1, 9):
            stairs[i][j] = (stairs[i-1][j+1] + stairs[i-1][j-1])
            stairs[i][j] = stairs[i][j] % 1000000000
        stairs[i][9] = stairs[i-1][8]
    result = 0
    for i in range(10):
        result += (stairs[N][i])
        result = result % 1000000000
    return result

print(solve())