import sys

def main():
    N = int(sys.stdin.readline().strip())
    matrix = [[0,0]]
    for _ in range(N):
        matrix.append(list(map(int, sys.stdin.readline().strip().split())))

    dp = [[0] * (N + 1) for i in range(N + 1)] # i번째 에서 j번째 까지 곱한 것
    for i in range(2, N + 1):
        for j in range(1, N - i + 2):
            dp[j][j+i-1] = min([dp[j][j + k] + dp[j + k + 1][j + i - 1] + (matrix[j][0] * matrix[j + k][1] * matrix[j + i - 1][1]) for k in range(i - 1)])




    print(dp[1][N])

if __name__ == "__main__":
    main()


"""inputs
3
5 3
3 2
2 6
"""
